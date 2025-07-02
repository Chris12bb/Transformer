
#!/usr/bin/env python3
"""
Main script for the Transformer project.
Company lookup using Yahoo Finance API.
"""

from utils import get_company_suggestions, format_company_suggestions


def get_company() -> str:
    """
    Get company information with autocomplete suggestions.
    
    Returns:
        str: Selected company symbol or name
    """
    while True:
        company_query = input("Enter a Company name or symbol (or 'quit' to exit): ").strip()
        
        if company_query.lower() == 'quit':
            return ""
        
        if not company_query:
            print("Please enter a valid company name or symbol.")
            continue
            
        print(f"\nSearching for companies matching '{company_query}'...")
        suggestions = get_company_suggestions(company_query)
        
        if suggestions:
            format_company_suggestions(suggestions)
            
            # Let user select from suggestions
            try:
                choice = input("\nEnter the number of your choice (or press Enter to search again): ").strip()
                if not choice:
                    continue
                    
                choice_num = int(choice)
                if 1 <= choice_num <= len(suggestions):
                    selected = suggestions[choice_num - 1]
                    symbol = selected['symbol']
                    name = selected['name']
                    print(f"\nSelected: {symbol} - {name}")
                    return symbol
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No companies found. Please try a different search term.")


def main():
    """Main function to run the script."""
    print("=== Company Lookup Tool ===")
    print("Search for companies using Yahoo Finance data")
    print()
    
    company_symbol = get_company()
    
    if company_symbol:
        print(f"\nFinal selection: {company_symbol}")
        print("You can now use this symbol for further analysis!")
    else:
        print("No company selected. Goodbye!")


if __name__ == "__main__":
    main()
