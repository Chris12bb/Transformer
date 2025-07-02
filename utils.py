#!/usr/bin/env python3
"""
Utility functions for the Transformer project.
"""

import requests


from typing import List, Dict, Optional


def get_company_suggestions(query: str) -> List[Dict[str, str]]:
    """
    Get company suggestions from Yahoo Finance API.
    
    Args:
        query (str): The company name or symbol to search for
        
    Returns:
        List[Dict[str, str]]: List of company suggestions with symbol and name
    """
    if not query or len(query.strip()) < 1:
        return []
    
    url = "https://yfapi.net/v6/finance/autocomplete"
    params = {
        "query": query.strip(),
        "lang": "en"
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        suggestions = []
        
        # Extract relevant company information
        if "quotes" in data:
            for quote in data["quotes"]:
                if quote.get("typeDisp") == "Equity":  # Only get stocks/equities
                    suggestions.append({
                        "symbol": quote.get("symbol", ""),
                        "name": quote.get("shortname", quote.get("longname", "")),
                        "exchange": quote.get("exchange", "")
                    })
        
        return suggestions[:10]  # Return top 10 suggestions
        
    except requests.RequestException as e:
        print(f"Error fetching company suggestions: {e}")
        return []
    except ValueError as e:
        print(f"Error parsing response: {e}")
        return []


def format_company_suggestions(suggestions: List[Dict[str, str]]) -> None:
    """
    Display company suggestions in a formatted way.
    
    Args:
        suggestions (List[Dict[str, str]]): List of company suggestions
    """
    if not suggestions:
        print("No company suggestions found.")
        return
    
    print("\nCompany Suggestions:")
    print("-" * 50)
    for i, company in enumerate(suggestions, 1):
        symbol = company.get("symbol", "N/A")
        name = company.get("name", "N/A")
        exchange = company.get("exchange", "N/A")
        print(f"{i:2d}. {symbol:8s} | {name[:30]:30s} | {exchange}")
    print("-" * 50)
