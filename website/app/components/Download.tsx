"use client";

import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { AppWindow as Windows, Apple, Link as Linux } from "lucide-react";
import { useEffect, useState } from "react";
import { detectPlatform, getPlatformDownloadUrl } from "@/lib/platform-utils";
import {
  hasValidKoFiSupportLink,
  hasValidSupporterPaymentLink,
  koFiSupportLink,
  supporterPaymentLink,
  trackMonetizationEvent,
} from "@/lib/monetization";

const downloads = [
  {
    icon: Windows,
    name: "Windows",
    version: "Latest",
  },
  {
    icon: Apple,
    name: "macOS",
    version: "Latest",
  },
  {
    icon: Linux,
    name: "Linux",
    version: "Latest",
  },
];

export function Download() {
  const [latestRelease, setLatestRelease] = useState<any>(null);
  const [userPlatform, setUserPlatform] = useState<string>("PC");

  useEffect(() => {
    // Detect user's platform
    setUserPlatform(detectPlatform());

    // Fetch latest release from GitHub
    fetch("https://api.github.com/repos/takeyamayuki/NonMouse/releases/latest")
      .then((res) => res.json())
      .then((data) => {
        setLatestRelease(data);
      })
      .catch((error) => {
        console.error("Error fetching release:", error);
      });
  }, []);

  const handleDownload = (platform: string) => {
    trackMonetizationEvent("download_cta_click", { placement: "download_section", platform });
    const url = getPlatformDownloadUrl(platform, latestRelease);
    if (url) {
      window.location.href = url;
    }
  };

  const handleSupportClick = (provider: string) => {
    trackMonetizationEvent("support_cta_click", { placement: "download_section", provider });
  };

  return (
    <section className="py-24 bg-background">
      <div className="container px-4 mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold mb-4">Download NonMouse</h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Available for all major platforms. Download and start using NonMouse today.
          </p>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-8 max-w-4xl mx-auto">
          {downloads.map((platform, index) => {
            const isUserPlatform = platform.name === userPlatform;
            return (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                viewport={{ once: true }}
              >
                <Card className={`p-6 text-center hover:shadow-lg transition-shadow ${
                  isUserPlatform ? 'ring-2 ring-primary' : ''
                }`}>
                  <platform.icon className="w-16 h-16 mx-auto mb-4 text-primary" />
                  <h3 className="text-xl font-semibold mb-2">{platform.name}</h3>
                  <p className="text-sm text-muted-foreground mb-4">
                    {latestRelease ? latestRelease.tag_name : "Loading..."}
                  </p>
                  <Button 
                    className="w-full"
                    onClick={() => handleDownload(platform.name)}
                  >
                    {isUserPlatform ? "Download for your system" : "Download"}
                  </Button>
                </Card>
              </motion.div>
            );
          })}
        </div>

        <motion.div
          id="support"
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          viewport={{ once: true }}
          className="max-w-4xl mx-auto mt-12 scroll-mt-24"
        >
          <Card className="p-8 border-primary/20 bg-primary/5">
            <div className="grid grid-cols-1 md:grid-cols-[1fr_auto] gap-6 items-center">
              <div>
                <h3 className="text-2xl font-bold mb-3">Support NonMouse development</h3>
                <p className="text-muted-foreground leading-relaxed">
                  We are exploring a native rebuild of NonMouse so gesture control can become more accurate, responsive, and comfortable in daily use.
                  If you want to help keep the project moving, support NonMouse with any amount on Buy Me a Coffee or Ko-fi.
                  Please include your email address or SNS ID in the message/details field so we can contact you when early access becomes available.
                </p>
              </div>
              <div className="flex flex-col items-center gap-3">
                {hasValidSupporterPaymentLink ? (
                  <a
                    href={supporterPaymentLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group inline-flex w-full max-w-[360px] rounded-xl leading-none transition-transform hover:-translate-y-0.5 active:translate-y-0"
                    onClick={() => handleSupportClick("buy_me_a_coffee")}
                  >
                    <img
                      src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png"
                      alt="Buy Me a Coffee"
                      className="block h-auto w-full rounded-xl shadow-sm transition-all group-hover:scale-[1.02] group-hover:opacity-90 group-hover:shadow-md"
                    />
                  </a>
                ) : null}
                {hasValidKoFiSupportLink ? (
                  <a
                    href={koFiSupportLink}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="group inline-flex h-[95px] w-full max-w-[360px] items-center justify-center gap-4 rounded-xl border border-border bg-card px-6 py-4 text-xl font-bold text-foreground shadow-sm transition-all hover:-translate-y-0.5 hover:bg-accent hover:shadow-md active:translate-y-0 md:h-[60px] md:text-base"
                    onClick={() => handleSupportClick("ko_fi")}
                  >
                    <img
                      src="https://storage.ko-fi.com/cdn/cup-border.png"
                      alt="Ko-fi cup icon"
                      className="h-12 w-auto transition-transform group-hover:scale-110 md:h-8"
                    />
                    <span>Support on Ko-fi</span>
                  </a>
                ) : null}
                {!hasValidSupporterPaymentLink && !hasValidKoFiSupportLink ? (
                  <Button
                    size="lg"
                    className="w-full md:w-auto"
                    disabled
                    title="Set NEXT_PUBLIC_BUY_ME_A_COFFEE_LINK or NEXT_PUBLIC_KO_FI_LINK to enable support."
                  >
                    Support coming soon
                  </Button>
                ) : null}
              </div>
            </div>
          </Card>
        </motion.div>
      </div>
    </section>
  );
}