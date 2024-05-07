export default function POIListPage() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="grid gap-8 lg:grid-cols-2">
        <h1>
          POI Name
        </h1>
      </div>
      <div>
        <p>
          POI information text.
        </p>
      </div>
      <div>
        <a href="https://zzm.wroc.pl/obiektyzzmcp/ogrod-japonski-we-wroclawiu/">Więcej informacji</a>
      </div>
      <div>
        <ol>
          <li>
            Comment 1
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
