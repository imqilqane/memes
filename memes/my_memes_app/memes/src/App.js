import {Route, BrowserRouter, Routes} from 'react-router-dom'
import { transitions, positions, Provider as AlertProvider } from 'react-alert'
import AlertTemplate from 'react-alert-template-basic'
import Header from './components/Header/Header'
import Home from './components/Home/Home'
import Singin from './components/Singin/Singin'
import Register from './components/Register/Register'
import Verify from './components/Register/Verify'
import Logout from './components/Logout/Logout'

const options = {
  // you can also just use 'bottom center'
  position: positions.BOTTOM_CENTER,
  timeout: 5000,
  offset: '30px',
  // you can also just use 'scale'
  transition: transitions.SCALE
}


function App() {
  return (
    <AlertProvider template={AlertTemplate} {...options}>
      <BrowserRouter>
        <Header />
        <Routes>
            <Route path="/" element={<Home />}></Route>
            <Route path="/login" element={<Singin />}></Route>
            <Route path="/logout" element={<Logout />}></Route>
            <Route path="/register" element={<Register />}></Route>
            <Route path="/register/verifing/:token" element={<Verify />}></Route>
        </Routes>
      </BrowserRouter>
    </AlertProvider>

  );
}

export default App;
