import { Link } from "react-router-dom";
import { ROUTE_LOGIN, ROUTE_REGISTER } from "../utils/consts";
import '../css/MainPage.css'; // Импортируем CSS файл

const MainPage = (): JSX.Element => (
  <>
    <div className="main-page">
      <div className="container mx-auto p-4">
        <h1 className="cloud-text">WELCOME TO CLOUD HAVEN</h1>
        <div>
          <Link to={ROUTE_LOGIN} className="text-blue-500">Login</Link> | 
          <Link to={ROUTE_REGISTER} className="text-blue-500"> Register</Link>
        </div>
      </div>
    </div>
  </>
);

export default MainPage;
