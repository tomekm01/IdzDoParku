export default function DashboardPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <div>
          <h1 className="text-3xl font-bold mb-4">Witaj Username!</h1>
        </div>
        <div className="flex flex-col space-y-4 lg:justify-center items-center">
          <a
            href="/poi_list"
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Lista POI
          </a>
          <a
            href="/ranking"
            className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Ranking
          </a>
        </div>
      </div>
      <footer className="mt-8">
        <p className="text-sm text-gray-500">
          © {new Date().getFullYear()} IdzDoParku. All rights reserved.
        </p>
      </footer>
    </div>
  );
}
