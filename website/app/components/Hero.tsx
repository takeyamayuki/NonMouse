"use client";

import { motion, useScroll, useTransform } from "framer-motion";
import Image from "next/image";
import { Button } from "@/components/ui/button";
import { ArrowRight, Github } from "lucide-react";
import { useRef, useEffect, useState } from "react";
import { getPlatformDownloadUrl } from "@/lib/platform-utils";
import {
  hasValidStripePaymentLink,
  stripePaymentLink,
  supporterPrice,
  trackMonetizationEvent,
} from "@/lib/monetization";

export function Hero() {
  const sectionRef = useRef<HTMLElement>(null);
  const { scrollYProgress } = useScroll({
    target: sectionRef,
    offset: ["start start", "end start"]
  });

  const [latestRelease, setLatestRelease] = useState<any>(null);
  const [userPlatform, setUserPlatform] = useState<string>("Unknown");

  useEffect(() => {
    const platform = navigator.platform.toLowerCase();
    if (platform.includes("win")) {
      setUserPlatform("Windows");
    } else if (platform.includes("mac")) {
      setUserPlatform("macOS");
    } else if (platform.includes("linux")) {
      setUserPlatform("Linux");
    }

    fetch("https://api.github.com/repos/takeyamayuki/NonMouse/releases/latest")
      .then((res) => res.json())
      .then((data) => {
        setLatestRelease(data);
      })
      .catch(console.error);
  }, []);

  const opacity = useTransform(scrollYProgress, [0, 1], [0.3, 0.1]);

  const handleDownload = () => {
    trackMonetizationEvent("download_cta_click", { placement: "hero" });
    const url = getPlatformDownloadUrl(userPlatform, latestRelease);
    if (url) {
      window.location.href = url;
    }
  };

  const handleSupportClick = () => {
    trackMonetizationEvent("support_cta_click", { placement: "hero" });
  };

  return (
    <section ref={sectionRef} className="relative min-h-screen flex items-center justify-center overflow-hidden">
      <div className="absolute inset-0 z-0">
        <div className="absolute inset-0 bg-gradient-to-b from-background via-background/95 to-background/90 z-10" />
      </div>

      {/* Enhanced grid pattern overlay with more visible grey accents */}
      <div className="absolute inset-0 overflow-hidden">
        {/* Primary grid */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#8882_1px,transparent_1px),linear-gradient(to_bottom,#8882_1px,transparent_1px)] bg-[size:14px_24px] [mask-image:radial-gradient(ellipse_60%_50%_at_50%_0%,#000_70%,transparent_100%)]" />
        
        {/* Secondary grid */}
        <div className="absolute inset-0 bg-[linear-gradient(to_right,#8882_1px,transparent_1px),linear-gradient(to_bottom,#8882_1px,transparent_1px)] bg-[size:80px_80px] [mask-image:radial-gradient(ellipse_80%_80%_at_50%_-20%,#000_40%,transparent_100%)]" />
        
        {/* Enhanced grey accent areas */}
        <div className="absolute inset-0">
          {/* Top-right accent - Made larger and more visible */}
          <div className="absolute top-[5%] right-[10%] w-[40vw] h-[30vh] bg-gray-400/[0.08] blur-2xl rounded-full" />
          
          {/* Bottom-left accent - Increased opacity */}
          <div className="absolute bottom-[15%] left-[5%] w-[35vw] h-[35vh] bg-gray-400/[0.06] blur-3xl rounded-full" />
          
          {/* Center accent - Made larger and more prominent */}
          <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[50vw] h-[40vh] bg-gray-400/[0.04] blur-3xl rounded-full" />
        </div>
        
        {/* Adjusted radial gradient overlay */}
        <div className="absolute inset-0 bg-gradient-to-b from-background/30 via-background/70 to-background/90" />
      </div>

      <div className="container px-4 mx-auto relative z-10">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
          <motion.div
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            transition={{ duration: 0.8 }}
            className="relative"
          >
            {/* Decorative elements */}
            <motion.div
              className="absolute -top-8 -left-8 w-32 h-32 bg-primary/5 rounded-full blur-3xl"
              animate={{
                scale: [1, 1.2, 1],
                opacity: [0.3, 0.5, 0.3],
              }}
              transition={{
                duration: 4,
                repeat: Infinity,
                repeatType: "reverse",
              }}
            />

            <motion.h1
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.2 }}
              className="text-5xl md:text-7xl font-bold mb-8 bg-clip-text text-transparent bg-gradient-to-r from-primary via-primary/90 to-primary/80 leading-[1.2] md:leading-[1.2]"
            >
              Intangible Mouse
            </motion.h1>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.4 }}
              className="text-lg md:text-xl mb-8 text-muted-foreground leading-relaxed"
            >
              Control your computer naturally with hand gestures. Transform your webcam into an intuitive mouse controller.
            </motion.p>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.8, delay: 0.6 }}
              className="flex flex-wrap gap-4"
            >
              <Button size="lg" className="text-lg px-8 group" onClick={handleDownload}>
                Download for {userPlatform}
                <ArrowRight className="ml-2 w-5 h-5 group-hover:translate-x-1 transition-transform" />
              </Button>
              {hasValidStripePaymentLink ? (
                <a
                  href={stripePaymentLink}
                  target="_blank"
                  rel="noopener noreferrer"
                  onClick={handleSupportClick}
                >
                  <Button size="lg" variant="secondary" className="text-lg px-8">
                    Support Early Access {supporterPrice}
                  </Button>
                </a>
              ) : (
                <Button
                  size="lg"
                  variant="secondary"
                  className="text-lg px-8"
                  disabled
                  title="Set NEXT_PUBLIC_STRIPE_PAYMENT_LINK to enable this checkout CTA."
                >
                  Support CTA coming soon
                </Button>
              )}
              <a
                href="https://github.com/takeyamayuki/NonMouse"
                target="_blank"
                rel="noopener noreferrer"
              >
                <Button size="lg" variant="outline" className="text-lg px-8">
                  <Github className="mr-2 w-5 h-5" />
                  View on GitHub
                </Button>
              </a>
            </motion.div>
          </motion.div>

          <motion.div
            initial={{ opacity: 0, scale: 0.95 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ duration: 0.8, delay: 0.2 }}
            className="block"
          >
            <div className="relative rounded-2xl overflow-hidden shadow-2xl bg-card border">
              <Image
                src="https://user-images.githubusercontent.com/22733958/135473409-9ddf2fc5-4722-4e55-8eef-64476635c10d.gif"
                alt="NonMouse gesture control demo"
                width={800}
                height={450}
                unoptimized
                className="w-full h-auto rounded-2xl"
              />
            </div>
          </motion.div>
        </div>
      </div>
    </section>
  );
}