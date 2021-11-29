import React, {useState} from 'react';
import axiosInstance from '../../axios';
import { useNavigate } from 'react-router-dom'
import {useAlert} from 'react-alert';

const Register = () => {
    const alert = useAlert();
    const navigate = useNavigate();
    const token = localStorage.getItem('access');
    const user_info = Object.freeze({
        username : "",
        email : "",
        password : "",
    });
    const [user, setUser] = useState(user_info);

    (!token || navigate('/'));

    const collectData = (e) => {
        setUser({...user , [e.target.name.trim()] : e.target.value.trim()});
        console.log(user);
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axiosInstance.post('auth/register/', user).then(res => {
            console.log(res.data);
            alert.show('successfully registerd please verify your account');
            navigate('/')
        }).catch(err => {
            console.log(err);
        })
    }
    return (
      
        <div className="singin">
        <p className="category">Home / Register</p>
        <div className="container">
            <div className="row">
            <div className="col-md-3"></div>

                <div className="col-md-6">
                    <form onSubmit={handleSubmit}>
                        <div className="row">
                            <input type="text" placeholder="your username" name="username" onChange={collectData} />
                        </div>
                        <div className="row">
                            <input type="email" placeholder="your email" name="email" onChange={collectData} />
                        </div>
                        <div className="row">
                            <input type="password" placeholder="your password" name="password" onChange={collectData}/>
                        </div>
                        <div className="row">
                            <button className="btn login">Register</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
        </div>
    );
};

export default Register;