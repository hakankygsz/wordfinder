import pandas as pd
import re
import sys
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def load_dataset(file_path='dataset.parquet'):
    try:
        df = pd.read_parquet(file_path)
        return df
    except FileNotFoundError:
        console.print("[bold red]⛔ Dataset bulunamadı![/bold red] Lütfen 'dataset.parquet' dosyasını bu dizine ekleyin.")
    except Exception as e:
        console.print(f"[bold red]💥 Dataset yüklenirken hata oluştu:[/bold red] {e}")
    return None

def search_word(df, search_term):
    if not search_term.strip():
        console.print("[yellow]⚠️ Lütfen geçerli bir kelime girin.[/yellow]")
        return

    result = df[df['word'].str.contains(re.escape(search_term), case=False, na=False)]

    if result.empty:
        console.print(Panel.fit(f"[cyan]'{search_term}'[/cyan] için bir sonuç bulunamadı 🧐", title="Bilgi", border_style="blue"))
    else:
        table = Table(title=f"🔍 Arama Sonuçları: [green]{search_term}[/green]", show_header=True, header_style="bold magenta")
        table.add_column("Kelime", style="bold white")
        table.add_column("Anlam", style="")

        for _, row in result.iterrows():
            table.add_row(row['word'], row['meaning'])

        console.print(table)

def main():
    df = load_dataset()
    if df is None:
        return

    console.print(Panel.fit(
        "[bold green]✨ Kelime Arama Arayüzüne Hoş Geldin! ✨[/bold green]\n[dim]Çıkmak için 'q', 'exit' veya Ctrl+C kullanabilirsin.[/dim]", 
            title="Developed By Hakan Kaygusuz", 
            border_style="green"
    ))

    try:
        while True:
            search_term = Prompt.ask("\n[bold cyan]Kelime ara[/bold cyan]")
            if search_term.lower() in {'q', 'exit', 'quit'}:
                console.print("[bold green]👋 Görüşmek üzere![/bold green]")
                break
            search_word(df, search_term)
    except KeyboardInterrupt:
        console.print("\n[bold yellow]🛑 Çıkış yapılıyor... Görüşürüz![/bold yellow]")

if __name__ == "__main__":
    main()
