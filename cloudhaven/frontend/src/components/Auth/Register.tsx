import { useData } from '../../ApiContext'; 

const Register = (): JSX.Element => {
  const { data, loading, error } = useData();

  return (
    <div>
      <h1>Register Page</h1>
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

export default Register;