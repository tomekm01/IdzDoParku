
import Image from 'next/image';

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen py-6 bg-gray-50">
      <div className="mb-8">
        <Image
          src="/logo.svg"
          alt="IdzDoParku Logo"
          width={300}
          height={100}
        />
      </div>
      <div className="grid gap-8 lg:grid-cols-2">
        <div>
          <h1 className="text-3xl font-bold mb-4">Witaj w IdzDoParku!</h1>
          <p className="text-lg">Twojej aplikacji do zwiedzania parków we Wrocławiu.</p>
          <p className="text-lg">Spaceruj, zbieraj punkty i zdobywaj osiągnięcia!</p>
        </div>
        <div className="flex flex-col space-y-4 lg:justify-center items-center">
          <a
            href="/login"
            className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Zaloguj się
          </a>
          <a
            href="/register"
            className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-lg transition-colors"
          >
            Rejestracja
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
