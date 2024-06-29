import { useData } from '../../ApiContext';

const Login = (): JSX.Element => {
  const { data, loading, error } = useData();

  return (
    <div>
      <h1>Login Page</h1>
      {loading && <p>Loading...</p>}
      {error && <p>Error: {error.message}</p>}
      {data && (
        <div>
          <h2>API Data:</h2>
          <pre>{JSON.stringify(data, null, 2)}</pre>
        </div>
      )}
    </div>
  );
};

export default Login;