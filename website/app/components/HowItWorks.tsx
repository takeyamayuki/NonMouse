"use client";

import { motion } from "framer-motion";
import { Card } from "@/components/ui/card";
import { Camera, MousePointer, Fingerprint, ArrowRight } from "lucide-react";

const steps = [
  {
    icon: Camera,
    title: "Enable Camera",
    description: "Allow NonMouse to access your webcam for hand tracking."
  },
  {
    icon: Fingerprint,
    title: "Hand Detection",
    description: "Our AI instantly recognizes and tracks your hand movements."
  },
  {
    icon: MousePointer,
    title: "Mouse Control",
    description: "Your hand movements are translated into precise cursor control."
  }
];

export function HowItWorks() {
  return (
    <section id="how-it-works" className="py-24 bg-accent/50">
      <div className="container px-4 mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold mb-4">How It Works</h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            Get started with NonMouse in three simple steps
          </p>
        </motion.div>
        <div className="flex flex-col md:flex-row justify-center items-center gap-8 max-w-5xl mx-auto">
          {steps.map((step, index) => (
            <motion.div
              key={index}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.2 }}
              viewport={{ once: true }}
              className="flex-1 relative"
            >
              <Card className="p-6 text-center h-full">
                <step.icon className="w-12 h-12 mx-auto mb-4 text-primary" />
                <h3 className="text-xl font-semibold mb-2">{step.title}</h3>
                <p className="text-muted-foreground">{step.description}</p>
              </Card>
              {index < steps.length - 1 && (
                <ArrowRight className="hidden md:block absolute top-1/2 -right-6 w-6 h-6 text-muted-foreground transform -translate-y-1/2" />
              )}
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}