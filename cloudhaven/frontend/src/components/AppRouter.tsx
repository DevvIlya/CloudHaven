import { Routes, Route } from 'react-router-dom';
import publicRoutes, { IPublicRoute } from '../routes';
import NotFoundPage from '../pages/NotFoundPage.tsx';
import MainPage from '../pages/MainPage';
import Login from '../components/Auth/Login';
import Register from '../components/Auth/Register';

const AppRouter = (): JSX.Element => (
  <main className='container'>
    <Routes>
      {publicRoutes.map(({ path, component: Component }: IPublicRoute) => (
        <Route key={path} path={path} element={<Component />} />
      ))
      }
      <Route path="*" element={<NotFoundPage />} />
      <Route path="/" element={<MainPage />} />
      <Route path="/login" element={<Login />} />
      <Route path="/register" element={<Register />} />
    </Routes>
  </main>
);

export default AppRouter;
