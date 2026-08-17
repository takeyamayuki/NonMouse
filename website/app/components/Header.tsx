"use client";

import { useState, useEffect } from "react";
import { motion } from "framer-motion";
import { Button } from "@/components/ui/button";
import { HandMetal } from "lucide-react";
import Image from "next/image";
import { detectPlatform, getPlatformDownloadUrl } from "@/lib/platform-utils";

export function Header() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [latestRelease, setLatestRelease] = useState<any>(null);
  const [userPlatform, setUserPlatform] = useState<string>("PC");

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener("scroll", handleScroll);

    // Detect platform and fetch latest release
    setUserPlatform(detectPlatform());

    fetch("https://api.github.com/repos/takeyamayuki/NonMouse/releases/latest")
      .then((res) => res.json())
      .then((data) => {
        setLatestRelease(data);
      })
      .catch(console.error);

    return () => window.removeEventListener("scroll", handleScroll);
  }, []);

  const scrollToSection = (id: string) => {
    const element = document.getElementById(id);
    if (element) {
      const headerOffset = 80;
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

      window.scrollTo({
        top: offsetPosition,
        behavior: "smooth"
      });
    }
  };

  const handleDownload = () => {
    const url = getPlatformDownloadUrl(userPlatform, latestRelease);
    if (url) {
      window.location.href = url;
    }
  };

  return (
    <motion.header
      className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${
        isScrolled ? "bg-background/80 backdrop-blur-md shadow-md" : "bg-transparent"
      }`}
      initial={{ y: -100 }}
      animate={{ y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-20">
          <div className="flex items-center space-x-3">
            <HandMetal className="w-8 h-8 text-primary" />
            <Image
              src="https://user-images.githubusercontent.com/22733958/183041432-cf6cc6f4-3a6f-4070-91a8-d0a7f7abf59f.JPG"
              alt="NonMouse Logo"
              width={200}
              height={66}
              className="h-8 w-auto"
            />
          </div>
          <nav className="hidden md:flex items-center space-x-8">
            <button
              onClick={() => scrollToSection("features")}
              className="text-foreground/80 hover:text-foreground transition-colors"
            >
              Features
            </button>
            <button
              onClick={() => scrollToSection("how-it-works")}
              className="text-foreground/80 hover:text-foreground transition-colors"
            >
              How It Works
            </button>
            <Button onClick={handleDownload}>
              Download for {userPlatform}
            </Button>
          </nav>
        </div>
      </div>
    </motion.header>
  );
}