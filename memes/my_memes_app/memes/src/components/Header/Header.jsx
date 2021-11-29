import React from 'react';
import { NavLink } from 'react-router-dom'; 
const Header = () => {
    return (
        <nav className='bg-secondary'>
            <ul class="nav justify-content-center">
                    <li className="nav-item">
                        <NavLink to="/" className="nav-link"><h5 className="text-light">Memes App</h5></NavLink>
                    </li>
                {
                    localStorage.getItem('access') ?
                    <>
                    
                    <li class="nav-item">
                        <NavLink to="/logout" className="text-light nav-link">Logout</NavLink>
                    </li>
                    </>
                    :
                    <>
                    <li class="nav-item">
                    <NavLink to="/login" className="text-light nav-link">SingIn</NavLink>
                    </li>

                    <li class="nav-item">
                        <NavLink to="/Register" className="text-light nav-link">Register</NavLink>
                    </li>
                    </>

                }
                
            </ul>
        </nav>
    );
};

export default Header;