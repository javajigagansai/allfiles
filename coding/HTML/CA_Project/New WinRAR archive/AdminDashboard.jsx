"import { useState, useEffect } from \"react\";
import { useNavigate } from \"react-router-dom\";
import { Button } from \"@/components/ui/button\";
import { Input } from \"@/components/ui/input\";
import { Label } from \"@/components/ui/label\";
import { Textarea } from \"@/components/ui/textarea\";
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from \"@/components/ui/dialog\";
import { toast } from \"sonner\";
import { SignOut, Plus, Pencil, Trash, Download, FileText } from \"@phosphor-icons/react\";
import axios from \"axios\";

const BACKEND_URL = process.env.REACT_APP_BACKEND_URL;
const API = `${BACKEND_URL}/api`;

export default function AdminDashboard() {
  const navigate = useNavigate();
  const [user, setUser] = useState(null);
  const [activeTab, setActiveTab] = useState('submissions');
  const [submissions, setSubmissions] = useState([]);
  const [services, setServices] = useState([]);
  const [editingService, setEditingService] = useState(null);
  const [newService, setNewService] = useState({ title: '', description: '', icon: 'receipt', order: 0 });

  useEffect(() => {
    fetchUser();
    fetchSubmissions();
    fetchServices();
  }, []);

  const fetchUser = async () => {
    try {
      const response = await axios.get(`${API}/auth/me`, { withCredentials: true });
      setUser(response.data);
      if (response.data.role !== 'admin') {
        navigate('/client/dashboard');
      }
    } catch (error) {
      navigate('/login');
    }
  };

  const fetchSubmissions = async () => {
    try {
      const response = await axios.get(`${API}/admin/submissions`, { withCredentials: true });
      setSubmissions(response.data);
    } catch (error) {
      console.error('Failed to fetch submissions:', error);
    }
  };

  const fetchServices = async () => {
    try {
      const response = await axios.get(`${API}/admin/services`, { withCredentials: true });
      setServices(response.data);
    } catch (error) {
      console.error('Failed to fetch services:', error);
    }
  };

  const handleLogout = async () => {
    try {
      await axios.post(`${API}/auth/logout`, {}, { withCredentials: true });
      navigate('/login');
    } catch (error) {
      navigate('/login');
    }
  };

  const handleCreateService = async () => {
    try {
      await axios.post(`${API}/admin/services`, newService, { withCredentials: true });
      toast.success('Service created successfully');
      setNewService({ title: '', description: '', icon: 'receipt', order: 0 });
      fetchServices();
    } catch (error) {
      toast.error('Failed to create service');
    }
  };

  const handleUpdateService = async (serviceId, updates) => {
    try {
      await axios.put(`${API}/admin/services/${serviceId}`, updates, { withCredentials: true });
      toast.success('Service updated successfully');
      setEditingService(null);
      fetchServices();
    } catch (error) {
      toast.error('Failed to update service');
    }
  };

  const handleDeleteService = async (serviceId) => {
    if (!window.confirm('Are you sure you want to delete this service?')) return;
    
    try {
      await axios.delete(`${API}/admin/services/${serviceId}`, { withCredentials: true });
      toast.success('Service deleted successfully');
      fetchServices();
    } catch (error) {
      toast.error('Failed to delete service');
    }
  };

  const handleDownloadDocument = async (path, filename) => {
    try {
      const response = await axios.get(`${API}/files/${path}`, {
        withCredentials: true,
        responseType: 'blob'
      });
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', filename);
      document.body.appendChild(link);
      link.click();
      link.remove();
      toast.success('Download started');
    } catch (error) {
      toast.error('Failed to download document');
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
              <span className=\"text-xs text-[#94A3B8]\">Admin Dashboard</span>
            </div>
          </div>
          
          <div className=\"flex items-center gap-4\">
            <div className=\"text-right hidden sm:block\">
              <p className=\"text-sm text-[#F8FAFC]\">{user?.name}</p>
              <p className=\"text-xs text-[#94A3B8]\">Administrator</p>
            </div>
            <Button
              onClick={handleLogout}
              variant=\"ghost\"
              size=\"icon\"
              className=\"text-[#94A3B8] hover:text-[#F8FAFC]\"
              data-testid=\"admin-logout-button\"
            >
              <SignOut size={20} />
            </Button>
          </div>
        </div>
      </header>

      <main className=\"container mx-auto px-6 py-12 max-w-7xl\">
        <div className=\"flex gap-4 mb-8 border-b border-white/10\">
          <button
            onClick={() => setActiveTab('submissions')}
            className={`px-6 py-3 font-medium transition-colors ${
              activeTab === 'submissions'
                ? 'text-[#D4AF37] border-b-2 border-[#D4AF37]'
                : 'text-[#94A3B8] hover:text-[#F8FAFC]'
            }`}
            data-testid=\"tab-submissions\"
          >
            Submissions
          </button>
          <button
            onClick={() => setActiveTab('services')}
            className={`px-6 py-3 font-medium transition-colors ${
              activeTab === 'services'
                ? 'text-[#D4AF37] border-b-2 border-[#D4AF37]'
                : 'text-[#94A3B8] hover:text-[#F8FAFC]'
            }`}
            data-testid=\"tab-services\"
          >
            Services
          </button>
        </div>

        {activeTab === 'submissions' && (
          <div className=\"bg-[#13161D] border border-white/10 rounded-lg p-8\" data-testid=\"submissions-panel\">
            <h2 className=\"font-heading text-3xl text-[#F8FAFC] mb-6\">Client Submissions</h2>
            
            {submissions.length === 0 ? (
              <p className=\"text-[#94A3B8] text-center py-8\">No submissions yet</p>
            ) : (
              <div className=\"space-y-4\">
                {submissions.map((submission) => (
                  <div
                    key={submission.submission_id}
                    className=\"bg-[#1A1F2A] border border-white/10 rounded-lg p-6\"
                    data-testid={`admin-submission-${submission.submission_id}`}
                  >
                    <div className=\"grid md:grid-cols-2 gap-4\">
                      <div>
                        <p className=\"text-xs text-[#94A3B8] tracking-[0.2em] uppercase mb-1\">Client Name</p>
                        <p className=\"text-[#F8FAFC] font-medium\">{submission.client_name}</p>
                      </div>
                      <div>
                        <p className=\"text-xs text-[#94A3B8] tracking-[0.2em] uppercase mb-1\">Email</p>
                        <p className=\"text-[#F8FAFC]\">{submission.client_email}</p>
                      </div>
                      {submission.dob && (
                        <div>
                          <p className=\"text-xs text-[#94A3B8] tracking-[0.2em] uppercase mb-1\">Date of Birth</p>
                          <p className=\"text-[#F8FAFC]\">{submission.dob}</p>
                        </div>
                      )}
                      {submission.gender && (
                        <div>
                          <p className=\"text-xs text-[#94A3B8] tracking-[0.2em] uppercase mb-1\">Gender</p>
                          <p className=\"text-[#F8FAFC] capitalize\">{submission.gender}</p>
                        </div>
                      )}
                      <div>
                        <p className=\"text-xs text-[#94A3B8] tracking-[0.2em] uppercase mb-1\">Submitted</p>
                        <p className=\"text-[#F8FAFC]\">{new Date(submission.submitted_at).toLocaleString()}</p>
                      </div>
                    </div>
                    
                    {submission.additional_info && (
                      <div className=\"mt-4\">
                        <p className=\"text-xs text-[#94A3B8] tracking-[0.2em] uppercase mb-1\">Additional Info</p>
                        <p className=\"text-[#F8FAFC] text-sm\">{submission.additional_info}</p>
                      </div>
                    )}
                    
                    {submission.document_path && (
                      <div className=\"mt-4\">
                        <Button
                          onClick={() => handleDownloadDocument(submission.document_path, submission.original_filename)}
                          variant=\"outline\"
                          size=\"sm\"
                          className=\"border-white/10 text-[#D4AF37] hover:bg-[#D4AF37]/10\"
                          data-testid={`download-${submission.submission_id}`}
                        >
                          <Download size={16} className=\"mr-2\" />
                          {submission.original_filename}
                        </Button>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            )}
          </div>
        )}

        {activeTab === 'services' && (
          <div className=\"bg-[#13161D] border border-white/10 rounded-lg p-8\" data-testid=\"services-panel\">
            <div className=\"flex justify-between items-center mb-6\">
              <h2 className=\"font-heading text-3xl text-[#F8FAFC]\">Manage Services</h2>
              
              <Dialog>
                <DialogTrigger asChild>
                  <Button className=\"bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10]\" data-testid=\"add-service-button\">
                    <Plus size={20} className=\"mr-2\" />
                    Add Service
                  </Button>
                </DialogTrigger>
                <DialogContent className=\"bg-[#1A1F2A] border-white/10 text-[#F8FAFC]\">
                  <DialogHeader>
                    <DialogTitle className=\"font-heading text-2xl\">Create New Service</DialogTitle>
                  </DialogHeader>
                  <div className=\"space-y-4\">
                    <div>
                      <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Title</Label>
                      <Input
                        value={newService.title}
                        onChange={(e) => setNewService({...newService, title: e.target.value})}
                        className=\"bg-[#13161D] border-white/10\"
                        data-testid=\"new-service-title\"
                      />
                    </div>
                    <div>
                      <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Description</Label>
                      <Textarea
                        value={newService.description}
                        onChange={(e) => setNewService({...newService, description: e.target.value})}
                        rows={3}
                        className=\"bg-[#13161D] border-white/10\"
                        data-testid=\"new-service-description\"
                      />
                    </div>
                    <div>
                      <Label className=\"text-[#94A3B8] text-xs tracking-[0.2em] uppercase mb-2 block\">Icon</Label>
                      <select
                        value={newService.icon}
                        onChange={(e) => setNewService({...newService, icon: e.target.value})}
                        className=\"w-full bg-[#13161D] border border-white/10 rounded-md px-3 py-2 text-[#F8FAFC]\"
                        data-testid=\"new-service-icon\"
                      >
                        <option value=\"receipt\">Receipt</option>
                        <option value=\"shield-check\">Shield Check</option>
                        <option value=\"chart-line-up\">Chart Line Up</option>
                        <option value=\"briefcase\">Briefcase</option>
                        <option value=\"calculator\">Calculator</option>
                      </select>
                    </div>
                    <Button
                      onClick={handleCreateService}
                      className=\"w-full bg-[#D4AF37] hover:bg-[#F0C94F] text-[#0A0C10]\"
                      data-testid=\"create-service-submit\"
                    >
                      Create Service
                    </Button>
                  </div>
                </DialogContent>
              </Dialog>
            </div>
            
            <div className=\"space-y-4\">
              {services.map((service) => (
                <div
                  key={service.service_id}
                  className=\"bg-[#1A1F2A] border border-white/10 rounded-lg p-6\"
                  data-testid={`service-item-${service.service_id}`}
                >
                  <div className=\"flex justify-between items-start\">
                    <div className=\"flex-1\">
                      <h3 className=\"font-heading text-xl text-[#F8FAFC] mb-2\">{service.title}</h3>
                      <p className=\"text-[#94A3B8] text-sm mb-2\">{service.description}</p>
                      <div className=\"flex gap-4 text-xs text-[#94A3B8]\">
                        <span>Icon: {service.icon}</span>
                        <span>Order: {service.order}</span>
                        <span className={service.is_active ? 'text-[#22C55E]' : 'text-[#EF4444]'}>
                          {service.is_active ? 'Active' : 'Inactive'}
                        </span>
                      </div>
                    </div>
                    <div className=\"flex gap-2\">
                      <Button
                        onClick={() => handleUpdateService(service.service_id, { is_active: !service.is_active })}
                        variant=\"outline\"
                        size=\"sm\"
                        className=\"border-white/10 text-[#94A3B8]\"
                        data-testid={`toggle-service-${service.service_id}`}
                      >
                        {service.is_active ? 'Deactivate' : 'Activate'}
                      </Button>
                      <Button
                        onClick={() => handleDeleteService(service.service_id)}
                        variant=\"outline\"
                        size=\"sm\"
                        className=\"border-white/10 text-[#EF4444] hover:bg-[#EF4444]/10\"
                        data-testid={`delete-service-${service.service_id}`}
                      >
                        <Trash size={16} />
                      </Button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
"