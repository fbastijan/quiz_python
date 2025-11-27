from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from quizapp.data.storage import load_questions
from quizapp.data.storage import load_players_and_scores
from quizapp.data.storage import save_player_and_score
from quizapp.data.storage import add_new_question
from quizapp.core.quiz_engine import QuizEngine

console = Console()

def run_cli():
    console.print("[bold cyan]===== KVIZ APLIKACIJA =====[/bold cyan]")

    while True:
        console.print("\n[yellow]1.[/yellow] Započni kviz")
        console.print("[yellow]2.[/yellow] Pokaži scoreboard")
        console.print("[yellow]3.[/yellow] Dodaj pitanje")
        console.print("[yellow]4.[/yellow] Exit")


        
        opcija = int(console.input("[bold]Odaberi opciju:[/bold] "))

        if opcija == 1:
            ime = str(console.input("Kako da te zovem? "))
            questions = load_questions()
            engine = QuizEngine(questions)
            engine.start()
            save_player_and_score(ime, engine.score)
            console.print(f"[green]✓ Hvala {ime}! Tvoj rezultat: {engine.score}[/green]")
        
        elif opcija == 2:
            players = load_players_and_scores()
            players = sorted(players, key=lambda x: int(x["score"]), reverse=True)
            
            table = Table(title="[bold cyan]SCOREBOARD[/bold cyan]")
            table.add_column("Pozicija", style="cyan")
            table.add_column("Ime", style="magenta")
            table.add_column("Score", style="green")
            
            for position, player in enumerate(players, start=1):
                table.add_row(str(position), player["name"], str(player["score"]))
            
            console.print(table)
        elif opcija == 3:
            console.print("\n[bold cyan]===== DODAJ NOVO PITANJE =====[/bold cyan]")
            
            question = {
                "category": "",
                "question": "",
                "options": [],
                "answer": ""
            }
            
            question["category"] = console.input("[yellow]Unesite kategoriju:[/yellow] ")
            question["question"] = console.input("[yellow]Unesite pitanje:[/yellow] ")
            
            for i in range(1, 4):
                option = console.input(f"[yellow]Unesite opciju {i}:[/yellow] ")
                question["options"].append(option)
            
            # Show options and ask for answer
            console.print("\n[cyan]Opcije:[/cyan]")
            for i, option in enumerate(question["options"], start=1):
                console.print(f"  {i}. {option}")
            
            answer_idx = int(console.input("[yellow]Koji je redni broj točnog odgovora? (1-3):[/yellow] ")) - 1
            question["answer"] = question["options"][answer_idx]
            
            add_new_question(question)
            console.print("[green]✓ Pitanje je uspješno dodano![/green]\n")
            
        elif opcija == 4:
            console.print("\n[bold green]Hvala što si igrao![/bold green]")
            break
        else:
            continue