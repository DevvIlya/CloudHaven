import React from 'react';
import publicRoutes, { IPublicRoute } from '../routes.ts';
import NotFoundPage from '../pages/NotFoundPage.tsx';
import { Routes, Route } from 'react-router-dom';

const AppRouter: React.FC = () => (
  <main className='container'>
    <Routes>
      {publicRoutes.map(({ path, component: Component }: IPublicRoute) => (
        <Route key={path} path={path} element={<Component />} />
      ))}
      <Route path="*" element={<NotFoundPage />} />
    </Routes>
  </main>
);

export default AppRouter;
