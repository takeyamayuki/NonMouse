"use client";

import { motion } from "framer-motion";
import Image from "next/image";

export function Demo() {
  return (
    <section id="demo" className="py-24 bg-accent">
      <div className="container px-4 mx-auto">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="text-center mb-16"
        >
          <h2 className="text-4xl font-bold mb-4">Seamless Integration</h2>
          <p className="text-lg text-muted-foreground max-w-2xl mx-auto">
            NonMouse integrates perfectly with your existing setup, providing a natural and intuitive experience.
          </p>
        </motion.div>
        <motion.div
          initial={{ opacity: 0, scale: 0.95 }}
          whileInView={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.8 }}
          viewport={{ once: true }}
          className="max-w-4xl mx-auto rounded-xl overflow-hidden"
        >
          <Image
            src="https://i.gyazo.com/098d853fe184b677b10a9c0e7716484a.png"
            alt="NonMouse Demo"
            width={800}
            height={600}
            className="w-full rounded-2xl"
            priority
          />
        </motion.div>
      </div>
    </section>
  );
}