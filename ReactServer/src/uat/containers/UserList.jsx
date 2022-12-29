import { useState, useEffect } from 'react'
import '../styles/UserList.css'
import axios from 'axios'
import ListForm from 'uat/components/ListForm'

export default function UserList(){
    const [list, setList] = useState([])
    useEffect(() => {
        axios
            .get('http://localhost:8000/blog/user-list')
            .then(res => {setList(res.data)})
            .catch(err => {
               console.log(err)
            })
    }, [])
         
    return (
    <>
      <ListForm list={list} style={{margin: "auto"}}/>
    </>
)}