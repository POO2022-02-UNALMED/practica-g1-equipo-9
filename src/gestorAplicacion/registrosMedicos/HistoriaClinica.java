package gestorAplicacion.registrosMedicos;
import gestorAplicacion.personas.Paciente;
import java.util.ArrayList;

public class HistoriaClinica {
    private Paciente paciente;
    private ArrayList<Diagnostico> diagnosticos;
    public static ArrayList<HistoriaClinica> historia= new ArrayList<HistoriaClinica>();
    
    public HistoriaClinica(Paciente paciente, ArrayList<Diagnostico> diagnosticos) {
        this.paciente = paciente;
        this.diagnosticos = diagnosticos;
    }

    public Paciente getPaciente() {
        return paciente;
    }

    public void setPaciente(Paciente paciente) {
        this.paciente = paciente;
    }

    public ArrayList<Diagnostico> getDiagnosticos() {
        return diagnosticos;
    }

    public void setDiagnosticos(ArrayList<Diagnostico> diagnosticos) {
        this.diagnosticos = diagnosticos;
    }

    public String visualizarDiagnostico(Diagnostico diagnosticos, int id) {
        return "El diagnostico es "+ diagnosticos + "El id del diagnostico es "+id;

    }
    public void crearHistoriaClinica(Paciente paciente, ArrayList<Diagnostico> diagnosticos){
        HistoriaClinica historia1 = new HistoriaClinica(paciente, diagnosticos);
        historia.add(historia1);
    }

    
}
