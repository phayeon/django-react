import { createSlice } from "@reduxjs/toolkit"
import { v4 as uuidv4 } from 'uuid'
/**
const initialState = {todos: [], todo: {}}

export const addTodoAction = todo => ({type: "ADD_TODO", payload: todo})
export const toggleTodoAction = todoId => ({type: "TOGGLE_TODE", payload: todoId})
export const deleteTodoAction = todoId => ({type: "DELETE_TODE", payload: todoId}) 


const todoReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'ADD_TODO':
        return {...state, todos: [...state.todos, action.payload]}
      case 'TOGGLE_TODE':
        return {...state, todos: state.todos.map(
            todo => (todo.id === action.payload) ? {...todo, complete: !todo.complete} 
                                                : todo)}
      case 'DELETE_TODE':
        return {...state, todos: state.todos.filter(todo => todo.id !== action.payload)}
      default:
        return state
    }
  }
 */
const todoSlice = createSlice({
  name: 'todos',
  initialState: [],
  reducers : {
    addTodo: (state, action) => {
      const newTodo = {
        id: uuidv4(),
        text: action.payload.text
      }
      state.push(newTodo)
    }, 
    deleteTodo: (state, action) => {
      return state.filter((todo) => todo.id !== action.payload.id)
    }
  }
})

export const { addTodo, deleteTodo } = todoSlice.actions

export default todoSlice.reducer