import axios from "axios";

const server = "http://localhost:3000/"
export const mplexMoviesFaces = req => axios.post(`${server}/movie/movies/faces`, req)