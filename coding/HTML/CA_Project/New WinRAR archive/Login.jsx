"import { useNavigate } from \"react-router-dom\";
import { Button } from \"@/components/ui/button\";

export default function Login() {
  const navigate = useNavigate();

  const handleLogin = () => {
    const redirectUrl = window.location.origin + '/client/dashboard';
    window.location.href = `https://auth.emergentagent.com/?redirect=${encodeURIComponent(redirectUrl)}`;
  };

  return (
    <div className=\"min-h-screen flex items-center justify-center bg-[#0A0C10] relative overflow-hidden\">
      <div className=\"absolute inset-0 bg-gradient-to-br from-[#D4AF37]/5 to-transparent pointer-events-none\"></div>
      
      <div className=\"relative z-10 max-w-md w-full mx-4\">
        <div className=\"bg-[#13161D]/80 backdrop-blur-xl border border-white/10 rounded-lg p-12 shadow-2xl\">
          <div className=\"text-center mb-8\">
            <h1 className=\"font-heading text-4xl text-[#F8FAFC] mb-2\" data-testid=\"login-heading\">
              Giri & Associates
            </h1>
            <p className=\"text-[#94A3B8] text-sm tracking-[0.2em] uppercase\">
              Chartered Accountants
            </p>
          </div>
          
          <div className=\"space-y-4\">
            <p className=\"text-[#94A3B8] text-center mb-6\">
              Sign in to access your portal
            </p>
            
            <Button
              onClick={handleLogin}
              className=\"w-full bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10] font-medium py-6 rounded-md transition-all hover:-translate-y-0.5 hover:shadow-lg hover:shadow-[#D4AF37]/20\"
              data-testid=\"google-login-button\"
            >
              Continue with Google
            </Button>
            
            <button
              onClick={() => navigate('/')}
              className=\"w-full text-[#94A3B8] hover:text-[#F8FAFC] text-sm py-2 transition-colors\"
              data-testid=\"back-to-home-button\"
            >
              Back to Home
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
"