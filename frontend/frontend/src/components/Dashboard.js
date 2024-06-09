import React from 'react';
import { useSelector } from 'react-redux';

const Dashboard = () => {
  const auth = useSelector(state => state.auth);

  if (!auth.isAuthenticated) {
    return <p>You need to log in to access this page.</p>;
  }

  return (
    <div>
      <h1>Welcome, {auth.user.fullName}!</h1>
      <p>This is your dashboard.</p>
    </div>
  );
};

export default Dashboard;
