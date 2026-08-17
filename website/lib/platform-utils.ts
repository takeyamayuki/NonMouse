export function getPlatformDownloadUrl(platform: string, latestRelease: any | null): string {
  if (!latestRelease) return "";

  if (platform === "PC" || platform === "Unknown") {
    return "https://github.com/takeyamayuki/NonMouse/releases/latest";
  }

  if (platform === "Linux") {
    return "https://github.com/takeyamayuki/NonMouse?tab=readme-ov-file#-pypi";
  }

  const pattern = platform === "Windows" ? /win/i : /mac/i;
  const asset = latestRelease.assets.find((asset: any) => pattern.test(asset.name));
  
  return asset ? asset.browser_download_url : "https://github.com/takeyamayuki/NonMouse/releases/latest";
}

export function detectPlatform(): string {
  if (typeof window === "undefined") return "PC";
  
  const platform = navigator.platform.toLowerCase();
  const userAgent = navigator.userAgent.toLowerCase();
  const isMobile = /iphone|ipad|ipod|android|mobile/.test(userAgent);
  if (isMobile) return "PC";

  if (platform.includes("win")) return "Windows";
  if (platform.includes("mac")) return "macOS";
  if (platform.includes("linux")) return "Linux";
  return "PC";
}