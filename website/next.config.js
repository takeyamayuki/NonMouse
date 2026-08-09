/** @type {import('next').NextConfig} */
const nextConfig = {
  output: 'export',
  allowedDevOrigins: ['yukimac-mini.tailb01472.ts.net'],
  images: { 
    unoptimized: true,
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'images.unsplash.com',
      },
      {
        protocol: 'https',
        hostname: 'i.gyazo.com',
      },
      {
        protocol: 'https',
        hostname: 'user-images.githubusercontent.com',
      }
    ],
  },
};

module.exports = nextConfig;