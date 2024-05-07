export default function POIListPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <h1>
          Username
        </h1>
      </div>
      <div>
      <ol>
          <li>
          <a
            href="/poi"
            className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            POI 1
          </a>
          </li>
        </ol>
      </div>
      <footer className="mt-8">
        <p className="text-sm text-gray-500">
          © {new Date().getFullYear()} IdzDoParku. All rights reserved.
        </p>
      </footer>
    </div>
  );
}
