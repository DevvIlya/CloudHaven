import axios from 'axios';

// Регистрация пользователя
export const registerUser = (userData) => async (dispatch) => {
  try {
    const response = await axios.post('/api/register', userData);
    dispatch({
      type: 'REGISTER_SUCCESS',
      payload: response.data,
    });
  } catch (error) {
    dispatch({
      type: 'REGISTER_FAIL',
      payload: error.response.data,
    });
  }
};

// Вход пользователя
export const loginUser = (userData) => async (dispatch) => {
  try {
    const response = await axios.post('/api/login', userData);
    dispatch({
      type: 'LOGIN_SUCCESS',
      payload: response.data,
    });
  } catch (error) {
    dispatch({
      type: 'LOGIN_FAIL',
      payload: error.response.data,
    });
  }
};
