import './App.css'
import { BrowserRouter } from 'react-router-dom'
import { ToastContainer } from 'react-toastify'
import AppRouter from './components/AppRouter'
import { DataProvider } from './ApiContext'

function App() {
  
  return (
    <DataProvider>  {/* Оберните приложение в DataProvider */}
      <BrowserRouter>
        <div className="container mx-auto">
          {/* <Header /> */}
          <AppRouter />
          {/* <Footer /> */}
        </div>
        <ToastContainer pauseOnFocusLoss />
      </BrowserRouter>
    </DataProvider>
  )
}

export default App

