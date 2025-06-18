"""

This script demonstrates the Proxy Design Pattern using a simple example of a video downloader.
A proxy is used to cache downloaded videos, avoiding repeated downloads of the same content.
"""

from abc import ABC, abstractmethod

# --- Subject Interface ---
class VideoDownloader(ABC):
    """
    The Subject interface that both RealDownloader and ProxyDownloader will implement.
    """
    @abstractmethod
    def download(self, url: str) -> str:
        pass


# --- Real Subject ---
class RealDownloader(VideoDownloader):
    """
    The real object that handles the actual video downloading.
    This simulates a resource-intensive operation.
    """
    def download(self, url: str) -> str:
        print(f"[RealDownloader] Downloading video from {url}...")
        return f"Video content from {url}"


# --- Proxy ---
class ProxyDownloader(VideoDownloader):
    """
    The proxy object that controls access to the RealDownloader.
    It caches previously downloaded videos to avoid repeated downloads.
    """
    def __init__(self):
        self.real_downloader = RealDownloader()
        self.cache = {}  # Dictionary to cache video content

    def download(self, url: str) -> str:
        if url in self.cache:
            print(f"[ProxyDownloader] Returning cached video for {url}.")
            return self.cache[url]
        else:
            print(f"[ProxyDownloader] No cache found. Downloading...")
            content = self.real_downloader.download(url)
            self.cache[url] = content
            return content


# --- Client Code ---
if __name__ == "__main__":
    # Create a proxy downloader
    downloader = ProxyDownloader()

    # Download videos
    video1 = downloader.download("http://example.com/video1")
    print(video1)

    video2 = downloader.download("http://example.com/video2")
    print(video2)

    # Try downloading video1 again to demonstrate caching
    video1_cached = downloader.download("http://example.com/video1")
    print(video1_cached)