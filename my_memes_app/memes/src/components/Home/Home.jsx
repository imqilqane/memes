import React, {useState, useEffect, useRef} from 'react';
import {useAlert} from 'react-alert';
import axios from "axios";
import '../../assets/css/home.css';


const Home = () => {

    const [meme, setMeme] = useState([]);
    const [pinedMeme, setPinedMeme] = useState([]);
    const [editedMeme, setEditedMeme] = useState([]);
    const myMemesOpen = useRef(false)
    const alert = useAlert();

    const generateMeme = () => {
        axios.get('https://api.chucknorris.io/jokes/random').then(
            res => {
                setMeme([res.data]);
            }
        ).catch(
            err => {
                console.log(err);
            }
        )
    };

    const pinMemeToMyMemes = (icon_url, meme_value) => {
        axios.post('http://localhost:8000/api-v1/memes/add/', {
            "icon_url": icon_url,
            "meme_value": meme_value,
        }).then(
            res => {
                alert.show('Successfully Added Tou Your Memes!');
                if (myMemesOpen.current) {
                    listMyMemes();
                }
            }
        ).catch(
            err => {
                console.log(err);
            }
        )
    };

    const listMyMemes = () => {
        axios.get('http://localhost:8000/api-v1/memes/all/').then(
            res => {
                setPinedMeme(res.data);
                myMemesOpen.current = true;
            }
        ).catch(
            err => {
                console.log(err);
            }
        )
    };

    const TarkEditeMeme = (e) => {
        setEditedMeme({...editedMeme,"icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png", "meme_value": e.target.value.trim(), })
    };

    const submitForm = id => event => {
        event.preventDefault()

        axios.put(`http://localhost:8000/api-v1/memes/edit/${id}/`,editedMeme).then(
            res => {
                alert.show('Successfully edited!');
                listMyMemes();
            }
        ).catch(
            err => {
                console.log(err);
            }
        )
    };

    const deleteMeme = (id, index) => {
        axios.delete(`http://localhost:8000/api-v1/memes/delete/${id}/`).then(
            res => {
                listMyMemes()
            }
        ).catch(
            err => {
                console.log(err);
            }
        )
    }

    return (
        <div>

            <main>
                <div className="container mt-5">
                    <div className="row ">
                        <div className="col-md-12">
                            <div className="row content">
                                <div className="col-md-12 mb-2">
                                    <button className="btn btn-success tell" onClick={generateMeme}>Tell me a jock</button>
                                    {
                                        meme.map((meme, index) => {
                                            return (
                                                <div className="row meme" key={index * Math.random()}>
                                                    <div className="col-md-1">
                                                        <img src={meme.icon_url} alt="" />
                                                    </div>
                                                    <div className="col-md-10">
                                                        <p>{meme.value}</p>
                                                    </div>
                                                    <div className="col-md-1">
                                                        <button className="btn btn-warning" onClick={() => pinMemeToMyMemes(meme.icon_url, meme.value)}>Pin</button>
                                                    </div>
                                                </div>
                                            )
                                        })
                                    }
                                </div>

                                <div className="col-md-12">
                                    <button className="btn btn-secondary show" onClick={listMyMemes}>My Memes</button>
                                    <ul>
                                        {
                                            pinedMeme.map((meme, index) => {
                                                return (
                                                    
                                                    <div className="row meme" key={meme.id}>
                                                        <div className="col-md-1">
                                                            <img src={meme.icon_url} alt="" />
                                                        </div>
                                                        <div className="col-md-10">
                                                            <form className="edit-meme-form" onSubmit={submitForm(meme.id)}>
                                                                <p>{meme.meme_value}</p>
                                                                <input type="text" defaultValue={meme.meme_value} name="meme_edited_value" onChange={TarkEditeMeme} />
                                                                <button className="btn btn-success">Edit</button>
                                                            </form>
                                                        </div>
                                                        <div className="col-md-1">
                                                            <button className="btn btn-danger" onClick={() => deleteMeme(meme.id, index)}>delete</button>
                                                        </div>
                                                    </div>
                                                )
                                            })
                                        }
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </main>
           
        </div>
    );
};

export default Home;