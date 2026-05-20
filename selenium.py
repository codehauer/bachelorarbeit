def scroll_down(self, driver: Firefox) -> bool:
        actions = ActionChains(driver)
        try:
            scroll_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".StandaloneInput-ScrollButton")))
            scroll_button.click()
            time.sleep(1)
            actions.scroll_by_amount(0, 500).perform()
            return True
        except:
            return False

    def prompt(self, message: str) -> str | None:
        options = FirefoxOptions()
        driver = webdriver.Firefox(options=options)

        response_text = None

        try:
            # Open the web interface
            driver.get(WEB_INTERFACE_URL)

            # Wait for the page to load (adjust time as needed)
            time.sleep(2)

            # Locate the input box (adjust the selector to match the web interface)
            # Update selector if necessary
            input_box = driver.find_element(
                By.CSS_SELECTOR, "textarea.AliceInput-Textarea")

            # Enter the prompt
            input_box.send_keys(message)
            input_box.send_keys(Keys.RETURN)  # Simulate pressing Enter

            # Wait for the response to load (adjust time as needed)
            time.sleep(1)

            copy_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "div.AliceChat-Message:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > menu:nth-child(1) > li:nth-child(1) > button:nth-child(1)")))
            self.scroll_down(driver)
            copy_button.click()

            time.sleep(1)

            # Get the copied content from clipboard
            response_text = pyperclip.paste()

        except:
            print(f"Failed to query: {message}")
        finally:
            # Close the browser
            driver.quit()

        return response_text
