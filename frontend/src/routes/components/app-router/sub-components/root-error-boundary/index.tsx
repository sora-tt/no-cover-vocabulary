import * as React from "react";
import { isRouteErrorResponse } from "react-router-dom";

import { useRootErrorBoundary } from "./hooks";

export const RootErrorBoundary: React.FC = () => {
  const { error } = useRootErrorBoundary();

  if (isRouteErrorResponse(error)) {
    return (
      <div>
        <h1>
          {error.status} - {error.statusText}
        </h1>
        {error.data?.message && <p>{error.data.message}</p>}
      </div>
    );
  }
  return <div>Something went wrong</div>;
};
