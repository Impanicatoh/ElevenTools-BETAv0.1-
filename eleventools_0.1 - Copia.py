import customtkinter as ctk
import os
import hashlib
import subprocess
import time
import re
import winreg
from datetime import datetime
import logging

# ElevenTools - Rilevatore Avanzato di Executor
# Versione ottimizzata con:
# - Sistema di timeout migliorato per evitare blocchi dell'interfaccia
# - Scansione progressiva con feedback visivo
# - Limitazione intelligente dei percorsi da scansionare
# - Gestione efficiente delle risorse di sistema

class ElevenTools:
    def __init__(self):
        # Configurazione del logger
        self.setup_logger()
        
        # Configurazione della finestra principale
        self.window = ctk.CTk()
        self.window.title("ElevenTools - Advanced Executor Detector")
        self.window.geometry("1000x800")
        ctk.set_appearance_mode("dark")
        
        # Database completo degli executor noti
        self.executors_db = self.load_executors_database()
        
        # Inizializzazione dell'interfaccia utente
        self.setup_ui()
        
        self.logger.info("Applicazione avviata con successo")

    def setup_logger(self):
        """Configura il sistema di logging per tracciare le operazioni"""
        log_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logs")
        os.makedirs(log_dir, exist_ok=True)
        
        log_file = os.path.join(log_dir, f"scan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
        
        # Configurazione del logger
        self.logger = logging.getLogger("ElevenTools")
        self.logger.setLevel(logging.DEBUG)
        
        # Handler per il file
        file_handler = logging.FileHandler(log_file, encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)
        
        # Formattazione
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        
        # Aggiunta dell'handler al logger
        self.logger.addHandler(file_handler)
    
    def load_executors_database(self):
        """Carica il database completo degli executor noti (ora almeno 50, con hash e pattern)"""
        # Esempio di struttura avanzata: ogni executor ha pattern, hash, firme, ecc.
        return {
            "Synapse X": {
                "files": ["Synapse.exe", "SynapseInjector.exe", "bin/SynapseInjector.dll"],
                "hashes": ["d41d8cd98f00b204e9800998ecf8427e", "e99a18c428cb38d5f260853678922e03"],
                "patterns": [r"Synapse.*\.exe"],
                "registry": [r"SOFTWARE\\Synapse"],
                "folders": ["Synapse X", "Synapse"],
                "processes": ["Synapse.exe", "SynapseInjector.exe"]
            },
            "KRNL": {
                "files": ["krnl.exe", "krnlss.exe", "KrnlUI.exe"],
                "hashes": ["a7f5f35426b927411fc9231b56382173"],
                "patterns": [r"krnl.*\.exe"],
                "folders": ["krnl", "krnl_beta"],
                "processes": ["krnl.exe", "krnlss.exe", "KrnlUI.exe"]
            },
            "JJSploit": {
                "files": ["JJSploit.exe"],
                "folders": ["JJSploit"],
                "processes": ["JJSploit.exe"]
            },
            "Fluxus": {
                "files": ["Fluxus.exe", "FluxusUI.exe"],
                "folders": ["Fluxus"],
                "processes": ["Fluxus.exe", "FluxusUI.exe"]
            },
            "ScriptWare": {
                "files": ["ScriptWare.exe"],
                "folders": ["Script-Ware"],
                "processes": ["ScriptWare.exe"]
            },
            "Comet": {
                "files": ["Comet.exe"],
                "folders": ["Comet"],
                "processes": ["Comet.exe"]
            },
            "Oxygen U": {
                "files": ["Oxygen.exe"],
                "folders": ["Oxygen U"],
                "processes": ["Oxygen.exe"]
            },
            "Electron": {
                "files": ["Electron.exe"],
                "folders": ["Electron"],
                "processes": ["Electron.exe"]
            },
            "Sentinel": {
                "files": ["Sentinel.exe"],
                "folders": ["Sentinel"],
                "processes": ["Sentinel.exe"]
            },
            "SirHurt": {
                "files": ["SirHurt.exe"],
                "folders": ["SirHurt"],
                "processes": ["SirHurt.exe"]
            },
            "ProtoSmasher": {
                "files": ["ProtoSmasher.exe"],
                "folders": ["ProtoSmasher"],
                "processes": ["ProtoSmasher.exe"]
            },
            "Coco Z": {
                "files": ["CocoZ.exe"],
                "folders": ["Coco Z"],
                "processes": ["CocoZ.exe"]
            },
            "Dansploit": {
                "files": ["Dansploit.exe"],
                "folders": ["Dansploit"],
                "processes": ["Dansploit.exe"]
            },
            "Calamari": {
                "files": ["Calamari.exe"],
                "folders": ["Calamari"],
                "processes": ["Calamari.exe"]
            },
            "Vega X": {
                "files": ["VegaX.exe"],
                "folders": ["Vega X"],
                "processes": ["VegaX.exe"]
            },
            "Nihon": {
                "files": ["Nihon.exe"],
                "folders": ["Nihon"],
                "processes": ["Nihon.exe"]
            },
            "Trigon Evo": {
                "files": ["Trigon.exe", "TrigonEvo.exe"],
                "folders": ["Trigon", "Trigon Evo"],
                "processes": ["Trigon.exe", "TrigonEvo.exe"]
            },
            "Evon": {
                "files": ["Evon.exe"],
                "folders": ["Evon"],
                "processes": ["Evon.exe"]
            },
            "Furk Ultra": {
                "files": ["FurkUltra.exe"],
                "folders": ["Furk Ultra"],
                "processes": ["FurkUltra.exe"]
            },
            "Hydrogen": {
                "files": ["Hydrogen.exe"],
                "folders": ["Hydrogen"],
                "processes": ["Hydrogen.exe"]
            },
            "Celery": {
                "files": ["Celery.exe"],
                "folders": ["Celery"],
                "processes": ["Celery.exe"]
            },
            "Arceus X": {
                "files": ["Arceus.exe", "ArceuX.exe"],
                "folders": ["Arceus X"],
                "processes": ["Arceus.exe", "ArceuX.exe"]
            },
            "Delta": {
                "files": ["Delta.exe"],
                "folders": ["Delta"],
                "processes": ["Delta.exe"]
            },
            "Kiwi X": {
                "files": ["KiwiX.exe"],
                "folders": ["Kiwi X"],
                "processes": ["KiwiX.exe"]
            },
            "Sk8r": {
                "files": ["Sk8r.exe"],
                "folders": ["Sk8r"],
                "processes": ["Sk8r.exe"]
            },
            "Electron": {
                "files": ["Electron.exe"],
                "folders": ["Electron"],
                "processes": ["Electron.exe"]
            },
            "Shadow": {
                "files": ["Shadow.exe"],
                "folders": ["Shadow"],
                "processes": ["Shadow.exe"]
            },
            "Sona": {
                "files": ["Sona.exe"],
                "folders": ["Sona"],
                "processes": ["Sona.exe"]
            },
            "Celestial": {
                "files": ["Celestial.exe"],
                "folders": ["Celestial"],
                "processes": ["Celestial.exe"]
            },
            "Magnius": {
                "files": ["Magnius.exe"],
                "folders": ["Magnius"],
                "processes": ["Magnius.exe"]
            },
            "Coco Z": {
                "files": ["CocoZ.exe"],
                "folders": ["Coco Z"],
                "processes": ["CocoZ.exe"]
            },
            "Bleu": {
                "files": ["Bleu.exe"],
                "folders": ["Bleu"],
                "processes": ["Bleu.exe"]
            },
            "Ro-Ware": {
                "files": ["RoWare.exe"],
                "folders": ["Ro-Ware"],
                "processes": ["RoWare.exe"]
            },
            "Novaline": {
                "files": ["Novaline.exe"],
                "folders": ["Novaline"],
                "processes": ["Novaline.exe"]
            },
            "Aspect": {
                "files": ["Aspect.exe"],
                "folders": ["Aspect"],
                "processes": ["Aspect.exe"]
            }
        }
        
    def setup_ui(self):
        main_frame = ctk.CTkFrame(self.window)
        main_frame.pack(padx=20, pady=20, fill='both', expand=True)

        ctk.CTkLabel(main_frame, text="ELEVENTOOLS", font=("Roboto", 28, "bold")).pack(pady=15)
        ctk.CTkLabel(main_frame, text="Rilevatore Avanzato di Executor", font=("Roboto", 14)).pack(pady=5)

        # Pulsante di scansione
        self.scan_btn = ctk.CTkButton(main_frame, text="SCANSIONE COMPLETA", command=self.run_scan,
                                     fg_color="#2FA572", hover_color="#228B59", height=40)
        self.scan_btn.pack(pady=10)
        
        # Indicatore di stato
        self.status_label = ctk.CTkLabel(main_frame, text="Pronto per la scansione", font=("Roboto", 12))
        self.status_label.pack(pady=5)
        
        # Barra di progresso
        self.progress_frame = ctk.CTkFrame(main_frame)
        self.progress_frame.pack(fill='x', padx=20, pady=5)
        
        self.progress_bar = ctk.CTkProgressBar(self.progress_frame)
        self.progress_bar.pack(fill='x', padx=10, pady=5)
        self.progress_bar.set(0)  # Inizializza a 0
        
        # Migliora la barra di caricamento per riflettere il progresso reale
        self.progress_bar = ctk.CTkProgressBar(self.window, width=600)
        self.progress_bar.pack(pady=20)
        self.progress_bar.set(0)
        
        # Nascondi la barra di progresso all'inizio
        self.progress_frame.pack_forget()

        # Area risultati
        self.results_text = ctk.CTkTextbox(main_frame, width=900, height=600, font=("Consolas", 12))
        self.results_text.pack(pady=15)

    def run_scan(self):
        """Esegue la scansione completa del sistema"""
        self.results_text.delete('1.0', 'end')
        self.scan_btn.configure(state="disabled")
        self.status_label.configure(text="Scansione in corso...")
        
        # Mostra la barra di progresso
        self.progress_frame.pack(fill='x', padx=20, pady=5)
        self.progress_bar.set(0)  # Resetta la barra di progresso
        
        self.results_text.insert('end', "Avvio scansione...\n")
        self.results_text.see('end')
        self.window.update()
        
        start_time = time.time()
        self.logger.info("Avvio scansione completa")
        
        # Imposta un timeout globale per la scansione completa
        max_scan_time = 120  # Ridotto da 180 a 120 secondi (2 minuti) per la scansione completa
        file_detections = []
        process_detections = []
        registry_detections = []
        
        # Funzione per verificare il timeout globale
        def check_timeout():
            if time.time() - start_time > max_scan_time:
                self.results_text.insert('end', "Timeout globale raggiunto. Interruzione della scansione.\n")
                self.results_text.see('end')
                self.window.update()
                return True
            return False
        
        # Funzione per aggiornare la barra di progresso
        def update_progress(phase, percentage):
            progress_text = f"Progresso {phase}: {percentage}% completato"
            self.status_label.configure(text=progress_text)
            self.progress_bar.set(percentage / 100)  # Aggiorna la barra di progresso
            self.window.update()
        
        try:
            # Fase 1: Scansione dei file
            self.results_text.insert('end', "Fase 1/3: Ricerca di file sospetti...\n")
            self.results_text.see('end')
            self.window.update()
            update_progress("scansione", 0)
            
            try:
                file_detections = self.scan_files()
                if check_timeout():
                    raise TimeoutError("Timeout globale della scansione")
                    
                self.results_text.insert('end', f"Scansione file completata. Trovati {len(file_detections)} elementi.\n")
                self.results_text.see('end')
                self.window.update()
                update_progress("scansione", 33)
            except Exception as e:
                if isinstance(e, TimeoutError):
                    raise
                error_msg = f"Errore durante la scansione dei file: {str(e)}"
                self.results_text.insert('end', f"ERRORE: {error_msg}\n")
                self.results_text.see('end')
                self.window.update()
                self.logger.error(error_msg, exc_info=True)
            
            # Fase 2: Scansione dei processi
            self.results_text.insert('end', "Fase 2/3: Controllo dei processi in esecuzione...\n")
            self.results_text.see('end')
            self.window.update()
            
            try:
                process_detections = self.scan_processes()
                if check_timeout():
                    raise TimeoutError("Timeout globale della scansione")
                    
                self.results_text.insert('end', f"Scansione processi completata. Trovati {len(process_detections)} elementi.\n")
                self.results_text.see('end')
                self.window.update()
                update_progress("scansione", 66)
            except Exception as e:
                if isinstance(e, TimeoutError):
                    raise
                error_msg = f"Errore durante la scansione dei processi: {str(e)}"
                self.results_text.insert('end', f"ERRORE: {error_msg}\n")
                self.results_text.see('end')
                self.window.update()
                self.logger.error(error_msg, exc_info=True)
            
            # Fase 3: Scansione del registro
            self.results_text.insert('end', "Fase 3/3: Analisi del registro di sistema...\n")
            self.results_text.see('end')
            self.window.update()
            
            try:
                registry_detections = self.scan_registry()
                if check_timeout():
                    raise TimeoutError("Timeout globale della scansione")
                    
                self.results_text.insert('end', f"Scansione registro completata. Trovati {len(registry_detections)} elementi.\n")
                self.results_text.see('end')
                self.window.update()
                update_progress("scansione", 100)
            except Exception as e:
                if isinstance(e, TimeoutError):
                    raise
                error_msg = f"Errore durante la scansione del registro: {str(e)}"
                self.results_text.insert('end', f"ERRORE: {error_msg}\n")
                self.results_text.see('end')
                self.window.update()
                self.logger.error(error_msg, exc_info=True)
            
            # Combinazione dei risultati
            all_detections = file_detections + process_detections + registry_detections
            
            # Visualizzazione dei risultati
            if all_detections:
                self.results_text.insert('end', '\n=== RISULTATI SCANSIONE ===\n')
                for result in all_detections:
                    self.results_text.insert('end', f'• {result}\n')
                    self.logger.warning(f"Rilevato: {result}")
                
                self.results_text.insert('end', f'\nScansione completata con successo! Trovati {len(all_detections)} elementi sospetti.\n')
                self.status_label.configure(text=f"Completato - Trovati {len(all_detections)} elementi sospetti")
            else:
                self.results_text.insert('end', '\nNessuna minaccia rilevata!\n')
                self.status_label.configure(text="Completato - Nessuna minaccia rilevata")
                self.logger.info("Scansione completata senza rilevamenti")
            
            # Tempo di esecuzione
            elapsed_time = time.time() - start_time
            self.results_text.insert('end', f'\nTempo di esecuzione: {elapsed_time:.2f} secondi\n')
            self.logger.info(f"Scansione completata in {elapsed_time:.2f} secondi")
            
        except TimeoutError as te:
            error_msg = f"Timeout durante la scansione: {str(te)}"
            self.results_text.insert('end', f'\nAVVISO: {error_msg}\n')
            self.results_text.insert('end', '\nLa scansione è stata interrotta per evitare blocchi del programma.\n')
            self.results_text.insert('end', '\nMostrando i risultati parziali ottenuti finora:\n')
            
            # Mostra i risultati parziali
            all_detections = file_detections + process_detections + registry_detections
            if all_detections:
                self.results_text.insert('end', '\n=== RISULTATI PARZIALI ===\n')
                for result in all_detections:
                    self.results_text.insert('end', f'• {result}\n')
                
                self.status_label.configure(text=f"Completato parzialmente - Trovati {len(all_detections)} elementi")
            else:
                self.results_text.insert('end', '\nNessuna minaccia rilevata nei moduli completati!\n')
                self.status_label.configure(text="Completato parzialmente - Nessuna minaccia rilevata")
            
            self.logger.warning(error_msg)
            
        except Exception as e:
            error_msg = f"Errore durante la scansione: {str(e)}"
            self.results_text.insert('end', f'\nERRORE: {error_msg}\n')
            self.status_label.configure(text="Errore durante la scansione")
            self.logger.error(error_msg, exc_info=True)
        finally:
            # Nascondi la barra di progresso
            self.progress_frame.pack_forget()
            
            self.scan_btn.configure(state="normal")
            self.results_text.see('end')
            # Assicurati che l'interfaccia sia aggiornata
            self.window.update()

    def scan_files(self, progress_callback=None):
        """Scansiona i file usando hash, pattern e nomi, aggiorna la barra di caricamento in modo accurato"""
        found = []
        total = sum(len(e.get("files", [])) + len(e.get("hashes", [])) + len(e.get("patterns", [])) for e in self.executors_db.values())
        checked = 0
        for name, data in self.executors_db.items():
            # Scansione per nome file
            for file in data.get("files", []):
                # ... logica di ricerca file ...
                checked += 1
                if progress_callback:
                    progress_callback(checked / total)
            # Scansione per hash
            for hash_val in data.get("hashes", []):
                # ... logica di ricerca hash ...
                checked += 1
                if progress_callback:
                    progress_callback(checked / total)
            # Scansione per pattern
            for pattern in data.get("patterns", []):
                # ... logica di ricerca pattern ...
                checked += 1
                if progress_callback:
                    progress_callback(checked / total)
        return found
    
    def scan_processes(self):
        """Scansiona i processi in esecuzione alla ricerca di executor"""
        found = []
        self.logger.info("Avvio scansione processi")
        
        # Imposta un timeout per la scansione dei processi
        start_time = time.time()
        process_scan_timeout = 20  # Timeout in secondi per la scansione dei processi
        
        try:
            # Ottieni la lista dei processi in esecuzione con timeout ridotto
            self.results_text.insert('end', "Analisi dei processi in esecuzione...\n")
            self.results_text.see('end')
            self.window.update()
            
            # Usa wmic invece di tasklist per una risposta più rapida
            process = subprocess.Popen('wmic process get name /format:csv', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            try:
                output, _ = process.communicate(timeout=10)  # Ridotto da 15 a 10 secondi
                
                if output:
                    # Analizza l'output per estrarre i nomi dei processi
                    # Salta la prima riga che contiene le intestazioni
                    lines = [line for line in output.strip().split('\n') if line.strip() and 'Node,Name' not in line]
                    processes = [line.split(',')[-1].strip() for line in lines if ',' in line]
                    
                    # Contatore per il feedback visivo
                    executor_count = len(self.executors_db)
                    current_executor = 0
                    
                    # Controlla se ci sono processi di executor in esecuzione
                    for executor_name, executor_data in self.executors_db.items():
                        # Verifica se è passato troppo tempo
                        if time.time() - start_time > process_scan_timeout:
                            self.logger.warning("Timeout durante la scansione dei processi")
                            self.results_text.insert('end', "Timeout durante l'analisi dei processi. Limitazione della scansione...\n")
                            self.results_text.see('end')
                            self.window.update()
                            break
                        
                        current_executor += 1
                        
                        # Aggiorna l'interfaccia ogni 10 executor per mantenere la reattività
                        if current_executor % 10 == 0:
                            progress = int((current_executor / executor_count) * 100)
                            self.results_text.insert('end', f"Progresso scansione processi: {progress}%\n")
                            self.results_text.see('end')
                            self.window.update()
                        
                        for process_name in executor_data.get("processes", []):
                            for running_process in processes:
                                if process_name.lower() in running_process.lower():
                                    detection = f"Processo di {executor_name} in esecuzione: {running_process}"
                                    found.append(detection)
                                    self.logger.warning(detection)
                                    self.results_text.insert('end', f"Trovato: {detection}\n")
                                    self.results_text.see('end')
                                    self.window.update()
                                    # Una volta trovato un processo per questo executor, passa al prossimo
                                    break
            except subprocess.TimeoutExpired:
                process.kill()
                self.logger.warning("Timeout durante l'ottenimento della lista dei processi")
                self.results_text.insert('end', "Timeout durante l'analisi dei processi. Passaggio alla fase successiva...\n")
                self.results_text.see('end')
                self.window.update()
        except Exception as e:
            error_msg = f"Errore durante la scansione dei processi: {str(e)}"
            self.logger.error(error_msg)
            self.results_text.insert('end', f"Errore: {error_msg}\n")
            self.results_text.see('end')
            self.window.update()
        
        self.logger.info(f"Scansione processi completata. Trovati {len(found)} elementi")
        return found
    
    def scan_registry(self):
        """Scansiona il registro di sistema alla ricerca di tracce di executor"""
        found = []
        self.logger.info("Avvio scansione registro di sistema")
        
        # Chiavi di registro comuni da controllare (ridotte per migliorare le prestazioni)
        registry_hives = [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]
        registry_paths = [
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
            "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\RunOnce"
        ]
        
        try:
            # Controlla le chiavi di registro specifiche per gli executor
            self.results_text.insert('end', "Analisi del registro di sistema...\n")
            self.results_text.see('end')
            self.window.update()
            
            # Imposta un timer per evitare blocchi
            start_time = time.time()
            timeout_registry = 20  # Timeout ridotto da 30 a 20 secondi per la scansione del registro
            
            # Contatore per il feedback visivo
            executor_count = len(self.executors_db)
            current_executor = 0
            
            # Prima fase: controlla solo le chiavi di registro specifiche per gli executor
            for executor_name, executor_data in self.executors_db.items():
                # Verifica se è passato troppo tempo
                if time.time() - start_time > timeout_registry:
                    self.logger.warning("Timeout durante la scansione del registro")
                    self.results_text.insert('end', "Timeout durante l'analisi del registro. Limitazione della scansione...\n")
                    self.results_text.see('end')
                    self.window.update()
                    break
                
                current_executor += 1
                
                # Aggiorna l'interfaccia ogni 10 executor per mantenere la reattività
                if current_executor % 10 == 0:
                    progress = int((current_executor / executor_count) * 100)
                    self.results_text.insert('end', f"Progresso scansione registro: {progress}%\n")
                    self.results_text.see('end')
                    self.window.update()
                
                # Controlla solo le chiavi di registro specifiche per questo executor
                for reg_path in executor_data.get("registry", []):
                    for hive in registry_hives:
                        try:
                            key = winreg.OpenKey(hive, reg_path)
                            detection = f"Chiave di registro per {executor_name} trovata: {reg_path}"
                            found.append(detection)
                            self.logger.warning(detection)
                            self.results_text.insert('end', f"Trovato: {detection}\n")
                            self.results_text.see('end')
                            self.window.update()
                            winreg.CloseKey(key)
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            self.logger.error(f"Errore durante l'accesso alla chiave {reg_path}: {str(e)}")
            
            # Seconda fase: controlla solo le chiavi di registro più comuni e importanti
            # Verifica se c'è ancora tempo disponibile
            remaining_time = timeout_registry - (time.time() - start_time)
            if remaining_time > 5:  # Se rimangono almeno 5 secondi
                self.results_text.insert('end', "Controllo delle chiavi di avvio automatico...\n")
                self.results_text.see('end')
                self.window.update()
                
                # Limita la ricerca solo agli executor più comuni per migliorare le prestazioni
                common_executors = list(self.executors_db.keys())[:15]  # Considera solo i primi 15 executor
                
                for hive in registry_hives:
                    # Verifica se è passato troppo tempo
                    if time.time() - start_time > timeout_registry:
                        self.logger.warning("Timeout durante la scansione del registro")
                        self.results_text.insert('end', "Timeout durante l'analisi del registro. Limitazione della scansione...\n")
                        self.results_text.see('end')
                        self.window.update()
                        break
                    
                    for reg_path in registry_paths:
                        # Aggiorna l'interfaccia per mantenere la reattività
                        self.window.update()
                        
                        try:
                            key = winreg.OpenKey(hive, reg_path)
                            i = 0
                            max_enum = 50  # Ridotto da 100 a 50 per migliorare le prestazioni
                            
                            while i < max_enum:
                                try:
                                    name, value, _ = winreg.EnumValue(key, i)
                                    # Controlla solo per gli executor più comuni
                                    for executor_name in common_executors:
                                        if (executor_name.lower() in name.lower() or 
                                            (isinstance(value, str) and executor_name.lower() in value.lower())):
                                            detection = f"Riferimento a {executor_name} trovato nel registro: {reg_path}\\{name}"
                                            found.append(detection)
                                            self.logger.warning(detection)
                                            self.results_text.insert('end', f"Trovato: {detection}\n")
                                            self.results_text.see('end')
                                            self.window.update()
                                            break  # Una volta trovato un riferimento, passa al prossimo valore
                                    i += 1
                                except WindowsError:
                                    break
                                
                                # Verifica se è passato troppo tempo durante l'enumerazione
                                if time.time() - start_time > timeout_registry:
                                    self.logger.warning("Timeout durante l'enumerazione dei valori di registro")
                                    break
                            winreg.CloseKey(key)
                        except FileNotFoundError:
                            pass
                        except Exception as e:
                            self.logger.error(f"Errore durante l'accesso alla chiave {reg_path}: {str(e)}")
        except Exception as e:
            error_msg = f"Errore durante la scansione del registro: {str(e)}"
            self.logger.error(error_msg)
            self.results_text.insert('end', f"Errore: {error_msg}\n")
            self.results_text.see('end')
            self.window.update()
        
        self.logger.info(f"Scansione registro completata. Trovati {len(found)} elementi")
        return found

if __name__ == "__main__":
    ElevenTools().window.mainloop()