"use client";

import { motion } from "framer-motion";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Camera, Aperture as Gesture, Keyboard, Laptop, Download, MousePointer } from "lucide-react";

const features = [
  {
    icon: Camera,
    title: "Minimal Requirements",
    description: "No need for anything other than a webcam and host PC. Get started with just your existing hardware."
  },
  {
    icon: Gesture,
    title: "Optimal Camera Position",
    description: "Gesture-based HCI has been around for some time, but shooting from above makes the mouse easier to use."
  },
  {
    icon: Keyboard,
    title: "Global Hotkey Access",
    description: "NonMouse can be invoked by the global hotkey even when this application is inactive."
  },
  {
    icon: Laptop,
    title: "Seamless Typing Integration",
    description: "Works well with typing, allowing for smooth transitions between gesture control and keyboard input."
  },
  {
    icon: Download,
    title: "Easy Installation",
    description: "Just download from the latest release. Currently available for Windows and macOS."
  },
  {
    icon: MousePointer,
    title: "Precise Control",
    description: "Advanced hand tracking ensures accurate cursor movement and gesture recognition."
  }
];

export function Features() {
  return (
    <section id="features" className="py-24 bg-background">
      <div className="container px-4 mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold mb-4">Features</h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Experience the future of computer interaction with our innovative features.
          </p>
        </motion.div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {features.map((feature, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              viewport={{ once: true }}
            >
              <Card className="h-full">
                <CardHeader>
                  <feature.icon className="w-12 h-12 mb-4 text-primary" />
                  <CardTitle>{feature.title}</CardTitle>
                </CardHeader>
                <CardContent>
                  <p className="text-muted-foreground">{feature.description}</p>
                </CardContent>
              </Card>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}