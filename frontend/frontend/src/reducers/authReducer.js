const initialState = {
    isAuthenticated: false,
    user: {},
    errors: {},
  };
  
  const authReducer = (state = initialState, action) => {
    switch (action.type) {
      case 'REGISTER_SUCCESS':
      case 'LOGIN_SUCCESS':
        return {
          ...state,
          isAuthenticated: true,
          user: action.payload,
          errors: {},
        };
      case 'REGISTER_FAIL':
      case 'LOGIN_FAIL':
        return {
          ...state,
          errors: action.payload,
        };
      default:
        return state;
    }
  };
  
  export default authReducer;
  