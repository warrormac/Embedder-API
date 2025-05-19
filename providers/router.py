# providers/router.py

from providers.local_provider import embedder as local_embedder
from providers.gateway_provider import embedder as gateway_embedder

class EmbedderRouter:
    def __init__(self, strategy="local"):
        self.strategy = strategy.lower()
        print(f"🧭 [ROUTER INIT] Strategy: {self.strategy}")

    def embed(self, text: str):
        if self.strategy == "both":
            print("🔁 [ROUTER] Running both local and gateway for embed...")
            local_result = self._try_embed(local_embedder, text, "local")
            gateway_result = self._try_embed(gateway_embedder, text, "gateway")
            self._log_result_summary(local_result, gateway_result)
            return local_result or gateway_result

        elif self.strategy == "gateway":
            return self._try_embed(gateway_embedder, text, "gateway")

        else:  # default to local
            return self._try_embed(local_embedder, text, "local")

    def batch_embed(self, texts: list):
        if self.strategy == "both":
            print("🔁 [ROUTER] Running both local and gateway for batch_embed...")
            local_result = self._try_batch(local_embedder, texts, "local")
            gateway_result = self._try_batch(gateway_embedder, texts, "gateway")
            self._log_result_summary(local_result, gateway_result)
            return local_result or gateway_result

        elif self.strategy == "gateway":
            return self._try_batch(gateway_embedder, texts, "gateway")

        else:  # default to local
            return self._try_batch(local_embedder, texts, "local")

    def _try_embed(self, provider, text, label):
        try:
            print(f"➡️ [ROUTER] {label}: embed()")
            return provider.embed(text)
        except Exception as e:
            print(f"❌ [ROUTER] {label} embedder failed: {e}")
            return None

    def _try_batch(self, provider, texts, label):
        try:
            print(f"➡️ [ROUTER] {label}: batch_embed()")
            return provider.batch_embed(texts)
        except Exception as e:
            print(f"❌ [ROUTER] {label} batch_embed failed: {e}")
            return []

    def _log_result_summary(self, local_result, gateway_result):
        local_ok = bool(local_result)
        gateway_ok = bool(gateway_result)

        print("\n📊 [ROUTER RESULT SUMMARY]")
        if local_ok and gateway_ok:
            print("✅ Both local and gateway succeeded.")
        elif local_ok:
            print("✅ Only local succeeded.")
        elif gateway_ok:
            print("✅ Only gateway succeeded.")
        else:
            print("❌ Both local and gateway failed.")
