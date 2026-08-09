export default function PrivacyPolicy() {
  return (
    <div className="min-h-screen bg-background py-24">
      <div className="container px-4 mx-auto max-w-4xl">
        <h1 className="text-4xl font-bold mb-8">Privacy Policy</h1>
        <p className="text-muted-foreground mb-8">Last updated: 2026-02-22</p>
        
        <div className="prose prose-lg max-w-none">
          <p className="mb-8">
            This Privacy Policy explains how ガチおすすめ ("the App") handles user data.
          </p>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">1. Data We Collect</h2>
          <p className="mb-4">
            The App collects only the data necessary to enable content publishing through the TikTok API:
          </p>
          <ul className="list-disc pl-6 mb-4">
            <li>OAuth access token</li>
            <li>OAuth refresh token</li>
            <li>TikTok account identifier (open_id)</li>
          </ul>
          <p className="mb-6">The App does not collect:</p>
          <ul className="list-disc pl-6 mb-8">
            <li>Passwords</li>
            <li>Direct messages</li>
            <li>Followers list</li>
            <li>Analytics data (unless explicitly granted by user)</li>
          </ul>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">2. How We Use Data</h2>
          <p className="mb-4">Collected data is used solely for:</p>
          <ul className="list-disc pl-6 mb-8">
            <li>Publishing videos on behalf of the user</li>
            <li>Managing scheduled content</li>
            <li>Maintaining authentication sessions</li>
          </ul>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">3. Data Storage</h2>
          <p className="mb-4">
            OAuth tokens are stored securely and are used only for API authentication.
          </p>
          <p className="mb-8">
            We do not sell, rent, or share user data with third parties.
          </p>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">4. Data Retention</h2>
          <p className="mb-4">
            OAuth tokens are retained only while the user actively uses the App.
          </p>
          <p className="mb-8">
            Users may request deletion of their data at any time.
          </p>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">5. Data Deletion Requests</h2>
          <p className="mb-4">
            To request deletion of stored authentication data, please contact:
          </p>
          <p className="mb-4">
            Email: <strong>kintre.ndy0@gmail.com</strong>
          </p>
          <p className="mb-8">
            All user data will be permanently deleted within 7 days of request.
          </p>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">6. Third-Party Services</h2>
          <p className="mb-4">
            The App interacts only with the official TikTok API.
          </p>
          <p className="mb-8">
            The App does not use third-party analytics, tracking tools, or advertising networks.
          </p>

          <hr className="my-8" />

          <h2 className="text-2xl font-semibold mb-4">7. Changes to This Policy</h2>
          <p className="mb-8">
            We may update this Privacy Policy periodically. Continued use of the App constitutes acceptance of updates.
          </p>
        </div>
      </div>
    </div>
  );
}