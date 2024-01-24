document.addEventListener('DOMContentLoaded', function() {
    /*copying shortened link to clipboard*/

    const copyBtn = document.querySelector('.copy_link')
    const shortLink = document.querySelector('.shortened_link')

    const copyLink = async (e) => {
        e.preventDefault()
        let text = shortLink.textContent
        
        try {
            await navigator.clipboard.writeText(text);
            /*change text and color of button*/
            copyBtn.innerHTML = 'Copied!'
            copyBtn.style.backgroundColor = '#3A3054'
            console.log('Copied to clipboard')
        } catch(err) {
            console.err('Failed to copy')
        }
    }

    if (copyBtn) copyBtn.addEventListener('click', copyLink)

})