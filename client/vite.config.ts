import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],  server: {
    host: true, // needed for docker
    port: 5174,
    strictPort: true,
    watch: {
      usePolling: true
    }
  }
})
