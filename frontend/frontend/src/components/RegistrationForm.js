import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { registerUser } from '../actions/authActions';

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    fullName: '',
    email: '',
    password: '',
  });

  const [errors, setErrors] = useState({});
  const dispatch = useDispatch();

  const validateForm = () => {
    const newErrors = {};
    const { username, email, password } = formData;

    if (!/^[a-zA-Z][a-zA-Z0-9]{3,19}$/.test(username)) {
      newErrors.username = 'Username must be 4-20 characters long and start with a letter.';
    }
    if (!/\S+@\S+\.\S+/.test(email)) {
      newErrors.email = 'Email is invalid.';
    }
    if (!/(?=.*[A-Z])(?=.*\d)(?=.*\W).{6,}/.test(password)) {
      newErrors.password = 'Password must be at least 6 characters long, with one uppercase letter, one number, and one special character.';
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (validateForm()) {
      dispatch(registerUser(formData));
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Username</label>
        <input
          type="text"
          name="username"
          value={formData.username}
          onChange={handleChange}
        />
        {errors.username && <p>{errors.username}</p>}
      </div>
      <div>
        <label>Full Name</label>
        <input
          type="text"
          name="fullName"
          value={formData.fullName}
          onChange={handleChange}
        />
      </div>
      <div>
        <label>Email</label>
        <input
          type="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        {errors.email && <p>{errors.email}</p>}
      </div>
      <div>
        <label>Password</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
        {errors.password && <p>{errors.password}</p>}
      </div>
      <button type="submit">Register</button>
    </form>
  );
};

export default RegistrationForm;
