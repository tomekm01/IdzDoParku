Aplikacja webowa typu "zbierz je wszystkie" dotycząca punktów zainteresowań we wrocławskich parkach. 

https://idz-do-parku.vercel.app

Projekt składa się z backendu opartego na Python Django (w folderze IdzDoParkuDjango), oraz frontendu Next.js (folder src, public oraz pozostałe pliki).
#########################################################################################################
Jak uruchomić?

1. Należy zainstalować postgreSQL, utworzyć użytkownika "postgres" z hasłem "parks" oraz utworzyć pustą bazę danych o nazwie Parks.
(w przypadku innej konfiguracji użytkownika należy zmienić dane w settings.py w IdzDoParku/IdzDoParkuDjango/IdzDoParkuDjango)

2. Należy zainstalować potrzebne pakiety:
```bash
npm install
pip install django djangorestframework
pip install django-cors-headers
pip install psycopg2
```
3. Należy zapełnić bazę danych danymi:
   - Najpierw w folderze IdzDoParku/IdzDoParkuDjango utworzyć migracje do bazy:
      ```bash
      python manage.py makemigrations
      python manage.py migrate
      ```
   - Następnie do gotowej bazy danych można wysłać przykładowe dane:
      ```bash
      python populate_db.py
      ```
    
4. Teraz wystarczy uruchomić aplikację:
     - w folderze IdzDoParku/IdzDoParkuDjango
      ```bash
      # uruchamiamy backend
      python manage.py runserver
      ```
     - równocześcnie na drugim terminalu w folderze IdzDoParku
      ```bash
      # uruchamiamy frontend
      npm run dev
      ```
     - pod adresem http://localhost:3000 powinna być uruchomiona sprawna aplikacja, można zalogować się na przykładowe konto (login Agata, hasło agataparks)
       
#########################################################################################################
This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/basic-features/font-optimization) to automatically optimize and load Inter, a custom Google Font.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
