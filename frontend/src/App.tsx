import * as React from "react";

import { AppRouter } from "./routes/components/app-router";

import "./static/styles/App.css";

const App: React.FC = () => {
  return (
    <div className="App">
      <AppRouter />
    </div>
  );
};

export default App;
