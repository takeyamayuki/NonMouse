"use client";

import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { Card } from "@/components/ui/card";
import { AppWindow as Windows, Apple, Link as Linux } from "lucide-react";
import { useEffect, useState } from "react";
import { getPlatformDownloadUrl } from "@/lib/platform-utils";
import {
  hasValidStripePaymentLink,
  stripePaymentLink,
  supporterPrice,
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
  const [userPlatform, setUserPlatform] = useState<string>("Unknown");

  useEffect(() => {
    // Detect user's platform
    const platform = navigator.platform.toLowerCase();
    if (platform.includes("win")) {
      setUserPlatform("Windows");
    } else if (platform.includes("mac")) {
      setUserPlatform("macOS");
    } else if (platform.includes("linux")) {
      setUserPlatform("Linux");
    }

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

  const handleCheckoutClick = () => {
    trackMonetizationEvent("checkout_cta_click", { placement: "download_section" });
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
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
          viewport={{ once: true }}
          className="max-w-4xl mx-auto mt-12"
        >
          <Card className="p-8 border-primary/20 bg-primary/5">
            <div className="grid grid-cols-1 md:grid-cols-[1fr_auto] gap-6 items-center">
              <div>
                <h3 className="text-2xl font-bold mb-3">Early-access supporter license</h3>
                <p className="text-muted-foreground leading-relaxed">
                  Keep the open-source version free while testing whether users will pay for packaged builds, setup guidance, and continued development support.
                </p>
                <p className="text-3xl font-bold mt-4">{supporterPrice}</p>
              </div>
              {hasValidStripePaymentLink ? (
                <a
                  href={stripePaymentLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  onClick={handleCheckoutClick}
                >
                  <Button size="lg" className="w-full md:w-auto">
                    Proceed to checkout
                  </Button>
                </a>
              ) : (
                <Button
                  size="lg"
                  className="w-full md:w-auto"
                  disabled
                  title="Set NEXT_PUBLIC_STRIPE_PAYMENT_LINK to enable checkout."
                >
                  Checkout coming soon
                </Button>
              )}
            </div>
          </Card>
        </motion.div>
      </div>
    </section>
  );
}