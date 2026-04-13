"import { useState, useEffect } from \"react\";
import { useNavigate } from \"react-router-dom\";
import { Button } from \"@/components/ui/button\";
import { Receipt, ShieldCheck, ChartLineUp, Briefcase, Calculator } from \"@phosphor-icons/react\";
import axios from \"axios\";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

const iconMap = {
  receipt: Receipt,
  \"shield-check\": ShieldCheck,
  \"chart-line-up\": ChartLineUp,
  briefcase: Briefcase,
  calculator: Calculator
};

export default function Home() {
  const navigate = useNavigate();
  const [services, setServices] = useState([]);
  const [showDataForm, setShowDataForm] = useState(false);

  useEffect(() => {
    const fetchServices = async () => {
      try {
        const response = await axios.get(`${API}/services`);
        setServices(response.data);
      } catch (error) {
        console.error('Failed to fetch services:', error);
      }
    };
    fetchServices();
  }, []);

  return (
    <div className=\"min-h-screen bg-[#0A0C10] text-[#F8FAFC]\">
      <header className=\"sticky top-0 z-50 bg-black/60 backdrop-blur-xl border-b border-white/10\">
        <div className=\"container mx-auto px-6 py-4 flex items-center justify-between\">
          <div className=\"flex items-center gap-3\">
            <div className=\"w-10 h-10 bg-gradient-to-br from-[#D4AF37] to-[#F0C94F] rounded-full\"></div>
            <span className=\"font-heading text-xl text-[#F8FAFC]\">Giri & Associates</span>
          </div>
          
          <nav className=\"hidden md:flex items-center gap-8\">
            <a href=\"#services\" className=\"text-[#94A3B8] hover:text-[#F8FAFC] transition-colors text-sm\">
              Services
            </a>
            <a href=\"#contact\" className=\"text-[#94A3B8] hover:text-[#F8FAFC] transition-colors text-sm\">
              Contact
            </a>
          </nav>
          
          <div className=\"flex items-center gap-3\">
            <Button
              onClick={() => setShowDataForm(true)}
              variant=\"ghost\"
              className=\"text-[#94A3B8] hover:text-[#F8FAFC] hidden sm:inline-flex\"
              data-testid=\"header-data-form-button\"
            >
              Submit Data
            </Button>
            <Button
              onClick={() => navigate('/login')}
              className=\"bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10] px-6\"
              data-testid=\"header-login-button\"
            >
              Login
            </Button>
          </div>
        </div>
      </header>

      <section
        className=\"relative min-h-[600px] flex items-center justify-center px-6 py-24 bg-cover bg-center\"
        style={{
          backgroundImage: `url('https://images.unsplash.com/photo-1764609289774-2b767bb4e6f5?crop=entropy&cs=srgb&fm=jpg&ixid=M3w3NDk1Nzh8MHwxfHNlYXJjaHwzfHxtb2Rlcm4lMjBvZmZpY2UlMjBidWlsZGluZyUyMGFyY2hpdGVjdHVyZSUyMGRhcmslMjBuaWdodHxlbnwwfHx8fDE3NzQ3NjIyNjV8MA&ixlib=rb-4.1.0&q=85')`
        }}
        data-testid=\"hero-section\"
      >
        <div className=\"absolute inset-0 bg-black/70\"></div>
        
        <div className=\"relative z-10 max-w-4xl mx-auto text-center\">
          <h1 className=\"font-heading text-5xl sm:text-6xl lg:text-7xl tracking-tight mb-6 text-[#F8FAFC]\">
            Finance clarity,<br />compliance confidence.
          </h1>
          <p className=\"text-lg text-[#94A3B8] leading-relaxed max-w-2xl mx-auto mb-8\">
            Expert tax, audit, and advisory services designed for businesses seeking precision and growth.
          </p>
          <Button
            onClick={() => setShowDataForm(true)}
            className=\"bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10] px-8 py-6 text-lg font-medium rounded-md transition-all hover:-translate-y-1 hover:shadow-xl hover:shadow-[#D4AF37]/30\"
            data-testid=\"hero-cta-button\"
          >
            Get Started
          </Button>
        </div>
      </section>

      <section id=\"services\" className=\"py-24 px-6 bg-[#13161D]\">
        <div className=\"container mx-auto max-w-7xl\">
          <div className=\"text-center mb-16\">
            <h2 className=\"font-heading text-4xl sm:text-5xl text-[#F8FAFC] mb-4\">
              Featured Services
            </h2>
            <p className=\"text-[#94A3B8]\">Comprehensive financial solutions tailored to your needs</p>
          </div>
          
          <div className=\"grid md:grid-cols-2 lg:grid-cols-3 gap-6\" data-testid=\"services-grid\">
            {services.map((service) => {
              const IconComponent = iconMap[service.icon] || Receipt;
              return (
                <div
                  key={service.service_id}
                  className=\"bg-[#1A1F2A] border border-white/10 rounded-lg p-8 hover:-translate-y-1 transition-all hover:shadow-xl hover:shadow-[#D4AF37]/10 hover:border-[#D4AF37]/50\"
                  data-testid={`service-card-${service.service_id}`}
                >
                  <IconComponent size={40} className=\"text-[#D4AF37] mb-4\" weight=\"duotone\" />
                  <h3 className=\"font-heading text-xl text-[#F8FAFC] mb-3\">{service.title}</h3>
                  <p className=\"text-[#94A3B8] text-sm leading-relaxed\">{service.description}</p>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      <section id=\"contact\" className=\"py-24 px-6 bg-[#0A0C10]\">
        <div className=\"container mx-auto max-w-4xl\">
          <div className=\"bg-[#13161D] border border-white/10 rounded-lg p-12\">
            <h2 className=\"font-heading text-4xl text-[#F8FAFC] mb-8\">Get in Touch</h2>
            <div className=\"space-y-4 text-[#94A3B8]\">
              <p className=\"flex items-center gap-3\">
                <span className=\"text-[#D4AF37]\">Email:</span>
                <span>contact@giriassociates.com</span>
              </p>
              <p className=\"flex items-center gap-3\">
                <span className=\"text-[#D4AF37]\">Phone:</span>
                <span>+91 98765 43210</span>
              </p>
              <p className=\"flex items-center gap-3\">
                <span className=\"text-[#D4AF37]\">Hours:</span>
                <span>Monday - Saturday, 9:00 AM - 6:00 PM</span>
              </p>
            </div>
          </div>
        </div>
      </section>

      <footer className=\"bg-[#13161D] border-t border-white/10 py-8 px-6\">
        <div className=\"container mx-auto text-center text-[#94A3B8] text-sm\">
          <p>&copy; 2026 Giri & Associates. All rights reserved.</p>
        </div>
      </footer>

      {showDataForm && (
        <DataFormModal onClose={() => setShowDataForm(false)} />
      )}
    </div>
  );
}

function DataFormModal({ onClose }) {
  const navigate = useNavigate();
  
  return (
    <div className=\"fixed inset-0 z-50 flex items-center justify-center bg-black/80 backdrop-blur-sm p-4\">
      <div className=\"bg-[#13161D] border border-white/10 rounded-lg p-8 max-w-md w-full\">
        <h3 className=\"font-heading text-2xl text-[#F8FAFC] mb-4\">Authentication Required</h3>
        <p className=\"text-[#94A3B8] mb-6\">
          Please log in to submit your data and documents.
        </p>
        <div className=\"flex gap-3\">
          <Button
            onClick={() => navigate('/login')}
            className=\"flex-1 bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10]\"
            data-testid=\"modal-login-button\"
          >
            Log In
          </Button>
          <Button
            onClick={onClose}
            variant=\"outline\"
            className=\"flex-1 border-white/10 text-[#94A3B8] hover:text-[#F8FAFC]\"
            data-testid=\"modal-close-button\"
          >
            Cancel
          </Button>
        </div>
      </div>
    </div>
  );
}
"