import pytest

class TestInspect:
    """Inspect what's on screen"""
    
    def test_print_page_source(self, driver):
        """Print entire page structure"""
        import time
        time.sleep(2)  # Wait for app to load
        
        page_source = driver.page_source
        print("\n" + "="*50)
        print("PAGE SOURCE:")
        print("="*50)
        print(page_source)
        print("="*50)
        
        