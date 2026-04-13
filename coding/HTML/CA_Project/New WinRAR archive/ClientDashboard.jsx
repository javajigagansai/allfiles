"import { useState, useEffect } from \"react\";
import { useNavigate } from \"react-router-dom\";
import { Button } from \"@/components/ui/button\";
import { Input } from \"@/components/ui/input\";
import { Label } from \"@/components/ui/label\";
import { Textarea } from \"@/components/ui/textarea\";
import { RadioGroup, RadioGroupItem } from \"@/components/ui/radio-group\";
import { toast } from \"sonner\";
import { SignOut, Upload, FileText } from \"@phosphor-icons/react\";
import axios from \"axios\";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export default function ClientDashboard() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [submissions, setSubmissions] = useState([]);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    client_name: \"\",
    client_email: \"\",
    dob: \"\",
    gender: \"\",
    additional_info: \"\"
  });
  const [file, setFile] = useState(null);

  useEffect(() => {
    fetchUser();
    fetchSubmissions();
  }, []);

  const fetchUser = async () => {
    try {
      const response = await axios.get(`${API}/auth/me`, { withCredentials: true });
      setUser(response.data);
      setFormData(prev => ({
        ...prev,
        client_name: response.data.name || \"\",
        client_email: response.data.email || \"\"
      }));
    } catch (error) {
      console.error('Failed to fetch user:', error);
      navigate('/login');
    }
  };

  const fetchSubmissions = async () => {
    try {
      const response = await axios.get(`${API}/submissions/my`, { withCredentials: true });
      setSubmissions(response.data);
    } catch (error) {
      console.error('Failed to fetch submissions:', error);
    }
  };

  const handleLogout = async () => {
    try {
      await axios.post(`${API}/auth/logout`, {}, { withCredentials: true });
      navigate('/login');
    } catch (error) {
      console.error('Logout failed:', error);
      navigate('/login');
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const submitData = new FormData();
      submitData.append('submission', JSON.stringify(formData));
      
      Object.keys(formData).forEach(key => {
        submitData.append(key, formData[key]);
      });
      
      if (file) {
        submitData.append('file', file);
      }

      await axios.post(`${API}/submissions`, submitData, {
        withCredentials: true,
        headers: { 'Content-Type': 'multipart/form-data' }
      });

      toast.success('Submission successful!');
      setFormData({
        client_name: user?.name || \"\",
        client_email: user?.email || \"\",
        dob: \"\",
        gender: \"\",
        additional_info: \"\"
      });
      setFile(null);
      fetchSubmissions();
    } catch (error) {
      console.error('Submission failed:', error);
      toast.error('Submission failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className=\"min-h-screen bg-[#0A0C10]\">
      <header className=\"sticky top-0 z-50 bg-black/60 backdrop-blur-xl border-b border-white/10\">
        <div className=\"container mx-auto px-6 py-4 flex items-center justify-between\">
          <div className=\"flex items-center gap-3\">
            <div className=\"w-10 h-10 bg-gradient-to-br from-[#D4AF37] to-[#F0C94F] rounded-full\"></div>
            <div>
              <span className=\"font-heading text-lg text-[#F8FAFC] block\">Giri & Associates</span>
              <span className=\"text-xs text-[#94A3B8]\">Client Portal</span>
            </div>
          </div>
          
          <div className=\"flex items-center gap-4\">
            <div className=\"text-right hidden sm:block\">
              <p className=\"text-sm text-[#F8FAFC]\">{user?.name}</p>
              <p className=\"text-xs text-[#94A3B8]\">{user?.email}</p>
            </div>
            <Button
              onClick={handleLogout}
              variant=\"ghost\"
              size=\"icon\"
              className=\"text-[#94A3B8] hover:text-[#F8FAFC]\"
              data-testid=\"logout-button\"
            >
              <SignOut size={20} />
            </Button>
          </div>
        </div>
      </header>

      <main className=\"container mx-auto px-6 py-12 max-w-6xl\">
        <div className=\"grid lg:grid-cols-2 gap-8\">
          <div className=\"bg-[#13161D] border border-white/10 rounded-lg p-8\" data-testid=\"submission-form\">
            <h2 className=\"font-heading text-3xl text-[#F8FAFC] mb-6\">Submit Data</h2>
            
            <form onSubmit={handleSubmit} className=\"space-y-6\">
              <div>
                <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Client Name</Label>
                <Input
                  value={formData.client_name}
                  onChange={(e) => setFormData({...formData, client_name: e.target.value})}
                  required
                  className=\"bg-[#1A1F2A] border-white/10 text-[#F8FAFC]\"
                  data-testid=\"input-client-name\"
                />
              </div>

              <div>
                <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Email</Label>
                <Input
                  type=\"email\"
                  value={formData.client_email}
                  onChange={(e) => setFormData({...formData, client_email: e.target.value})}
                  required
                  className=\"bg-[#1A1F2A] border-white/10 text-[#F8FAFC]\"
                  data-testid=\"input-client-email\"
                />
              </div>

              <div>
                <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Date of Birth</Label>
                <Input
                  type=\"date\"
                  value={formData.dob}
                  onChange={(e) => setFormData({...formData, dob: e.target.value})}
                  className=\"bg-[#1A1F2A] border-white/10 text-[#F8FAFC]\"
                  data-testid=\"input-dob\"
                />
              </div>

              <div>
                <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Gender</Label>
                <RadioGroup
                  value={formData.gender}
                  onValueChange={(value) => setFormData({...formData, gender: value})}
                  className=\"flex gap-4\"
                >
                  <div className=\"flex items-center space-x-2\">
                    <RadioGroupItem value=\"male\" id=\"male\" data-testid=\"radio-male\" />
                    <Label htmlFor=\"male\" className=\"text-[#94A3B8] cursor-pointer\">Male</Label>
                  </div>
                  <div className=\"flex items-center space-x-2\">
                    <RadioGroupItem value=\"female\" id=\"female\" data-testid=\"radio-female\" />
                    <Label htmlFor=\"female\" className=\"text-[#94A3B8] cursor-pointer\">Female</Label>
                  </div>
                  <div className=\"flex items-center space-x-2\">
                    <RadioGroupItem value=\"other\" id=\"other\" data-testid=\"radio-other\" />
                    <Label htmlFor=\"other\" className=\"text-[#94A3B8] cursor-pointer\">Other</Label>
                  </div>
                </RadioGroup>
              </div>

              <div>
                <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Upload Document</Label>
                <div className=\"border-2 border-dashed border-white/10 rounded-lg p-6 text-center hover:border-[#D4AF37]/50 transition-colors\">
                  <input
                    type=\"file\"
                    onChange={(e) => setFile(e.target.files[0])}
                    className=\"hidden\"
                    id=\"file-upload\"
                    data-testid=\"file-input\"
                  />
                  <label htmlFor=\"file-upload\" className=\"cursor-pointer\">
                    <Upload size={32} className=\"mx-auto text-[#D4AF37] mb-2\" />
                    <p className=\"text-[#94A3B8] text-sm\">
                      {file ? file.name : 'Click to upload document'}
                    </p>
                  </label>
                </div>
              </div>

              <div>
                <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Additional Information</Label>
                <Textarea
                  value={formData.additional_info}
                  onChange={(e) => setFormData({...formData, additional_info: e.target.value})}
                  rows={4}
                  className=\"bg-[#1A1F2A] border-white/10 text-[#F8FAFC]\"
                  data-testid=\"textarea-additional-info\"
                />
              </div>

              <Button
                type=\"submit\"
                disabled={loading}
                className=\"w-full bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10] py-6 font-medium\"
                data-testid=\"submit-button\"
              >
                {loading ? 'Submitting...' : 'Submit'}
              </Button>
            </form>
          </div>

          <div className=\"bg-[#13161D] border border-white/10 rounded-lg p-8\" data-testid=\"submissions-list\">
            <h2 className=\"font-heading text-3xl text-[#F8FAFC] mb-6\">Your Submissions</h2>
            
            {submissions.length === 0 ? (
              <p className=\"text-[#94A3B8] text-center py-8\">No submissions yet</p>
            ) : (
              <div className=\"space-y-4\">
                {submissions.map((submission) => (
                  <div
                    key={submission.submission_id}
                    className=\"bg-[#1A1F2A] border border-white/10 rounded-lg p-6\"
                    data-testid={`submission-${submission.submission_id}`}
                  >
                    <div className=\"flex justify-between items-start mb-3\">
                      <h3 className=\"font-heading text-lg text-[#F8FAFC]\">{submission.client_name}</h3>
                      <span className=\"text-xs text-[#94A3B8]\">
                        {new Date(submission.submitted_at).toLocaleDateString()}
                      </span>
                    </div>
                    <p className=\"text-sm text-[#94A3B8] mb-2\">{submission.client_email}</p>
                    {submission.additional_info && (
                      <p className=\"text-sm text-[#94A3B8] mb-3\">{submission.additional_info}</p>
                    )}
                    {submission.document_path && (
                      <div className=\"flex items-center gap-2 text-[#D4AF37] text-sm\">
                        <FileText size={16} />
                        <span>{submission.original_filename}</span>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
"