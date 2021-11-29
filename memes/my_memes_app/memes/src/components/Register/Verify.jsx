import React, {useEffect, useState}  from 'react';
import { useParams } from 'react-router';
import axiosInstance from '../../axios';

const Verify = () => {
    const {token} = useParams();
    const [loading, setLoading] = useState(true)
    const [notVerify, setnotVerify] = useState(false)
    useEffect(() => {
        axiosInstance.get(`auth/register/verify/?token=${token}`).then(res => {
            console.log(res);
            setLoading(false);
        }).catch(err => {
            console.log(err);
            setnotVerify(true);
        })
    }, [])

    if (loading === 1) {
        return <div> loading </div>
    } else if (notVerify) {
        return <div> something went wrong please contact us </div>
    }

    return (
        <>
            <h2>Your account is successfully verified ... you can log in now</h2>
        </>
    );
};

export default Verify;