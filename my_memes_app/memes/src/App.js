import {Route, BrowserRouter, Routes} from 'react-router-dom'
import { transitions, positions, Provider as AlertProvider } from 'react-alert'
import AlertTemplate from 'react-alert-template-basic'
import { Provider } from 'react-redux';
import Header from './components/Header/Header'
import Home from './components/Home/Home'

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
        </Routes>
      </BrowserRouter>
    </AlertProvider>

  );
}

export default App;
