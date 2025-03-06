import AppRoutes from './routes/AppRoutes';
import AuthProvider  from './context/AuthContext';

function App() {
  return (
    <AuthProvider>
      <div>
        <AppRoutes />
      </div>
    </AuthProvider>
  );
}

export default App;
